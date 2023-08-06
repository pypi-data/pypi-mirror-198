use num_traits::AsPrimitive;

/// elastic potential energy (St.Venant-Kirchhoff material)
/// and its derivative and hessian w.r.t.
/// the deformed vertex position for a 3D triangle.
///
/// * `P` - undeformed triangle vertex positions
/// * `p` - deformed triangle vertex positions
/// * `lambda` - Lame's 1st parameter
/// * `myu` - Lame's 2nd parameter
#[allow(non_snake_case)]
pub fn wdwddw_cst<T>(
    dw: &mut [[T; 3]; 3],
    ddw: &mut [[[[T; 3]; 3]; 3]; 3],
    P: [[T; 3]; 3],
    p: [[T; 3]; 3],
    lambda: T,
    myu: T)
    -> T
where T: num_traits::Float + 'static + Copy + std::ops::MulAssign + std::ops::AddAssign,
      f32: num_traits::AsPrimitive<T>
{
    use del_geo::tri;
    use del_geo::vec3;

    let zero = T::zero();
    let one = T::one();
    let two = 2_f32.as_();
    let half = 0.5_f32.as_();

    let mut Gd: [[T; 3]; 3] = [ // undeformed edge vector
        [P[1][0] - P[0][0], P[1][1] - P[0][1], P[1][2] - P[0][2]],
        [P[2][0] - P[0][0], P[2][1] - P[0][1], P[2][2] - P[0][2]],
        [zero, zero, zero]];

    let Area: T = tri::unit_normal3(&mut Gd[2], &P[0], &P[1], &P[2]);

    let mut Gu: [[T; 3]; 2] = [[zero; 3]; 2]; // inverse of Gd
    {
        vec3::cross_mut(&mut Gu[0], &Gd[1], &Gd[2]);
        let invtmp1 = one / vec3::dot(&Gu[0], &Gd[0]);
        Gu[0][0] *= invtmp1;
        Gu[0][1] *= invtmp1;
        Gu[0][2] *= invtmp1;
        //
        vec3::cross_mut(&mut Gu[1], &Gd[2], &Gd[0]);
        let invtmp2 = one / vec3::dot(&Gu[1], &Gd[1]);
        Gu[1][0] *= invtmp2;
        Gu[1][1] *= invtmp2;
        Gu[1][2] *= invtmp2;
    }

    let gd: [[T; 3]; 2] = [ // deformed edge vector
        [p[1][0] - p[0][0], p[1][1] - p[0][1], p[1][2] - p[0][2]],
        [p[2][0] - p[0][0], p[2][1] - p[0][1], p[2][2] - p[0][2]]
    ];

    let E2: [T; 3] = [  // green lagrange strain (with engineer's notation)
        half * (vec3::dot(&gd[0], &gd[0]) - vec3::dot(&Gd[0], &Gd[0])),
        half * (vec3::dot(&gd[1], &gd[1]) - vec3::dot(&Gd[1], &Gd[1])),
        one * (vec3::dot(&gd[0], &gd[1]) - vec3::dot(&Gd[0], &Gd[1]))
    ];

    let GuGu2: [T; 3] = [
        vec3::dot(&Gu[0], &Gu[0]),
        vec3::dot(&Gu[1], &Gu[1]),
        vec3::dot(&Gu[1], &Gu[0])];

    let cons2: [[T; 3]; 3] = [ // constitutive tensor
        [
            lambda * GuGu2[0] * GuGu2[0] + two * myu * (GuGu2[0] * GuGu2[0]),
            lambda * GuGu2[0] * GuGu2[1] + two * myu * (GuGu2[2] * GuGu2[2]),
            lambda * GuGu2[0] * GuGu2[2] + two * myu * (GuGu2[0] * GuGu2[2])
        ],
        [
            lambda * GuGu2[1] * GuGu2[0] + two * myu * (GuGu2[2] * GuGu2[2]),
            lambda * GuGu2[1] * GuGu2[1] + two * myu * (GuGu2[1] * GuGu2[1]),
            lambda * GuGu2[1] * GuGu2[2] + two * myu * (GuGu2[2] * GuGu2[1])
        ],
        [
            lambda * GuGu2[2] * GuGu2[0] + two * myu * (GuGu2[0] * GuGu2[2]),
            lambda * GuGu2[2] * GuGu2[1] + two * myu * (GuGu2[2] * GuGu2[1]),
            lambda * GuGu2[2] * GuGu2[2] + one * myu * (GuGu2[0] * GuGu2[1] + GuGu2[2] * GuGu2[2])
        ]
    ];
    let S2: [T; 3] = [  // 2nd Piola-Kirchhoff stress
        cons2[0][0] * E2[0] + cons2[0][1] * E2[1] + cons2[0][2] * E2[2],
        cons2[1][0] * E2[0] + cons2[1][1] * E2[1] + cons2[1][2] * E2[2],
        cons2[2][0] * E2[0] + cons2[2][1] * E2[1] + cons2[2][2] * E2[2]
    ];

    // compute energy
    let w = half * Area * (E2[0] * S2[0] + E2[1] * S2[1] + E2[2] * S2[2]);

    // compute 1st derivative
    let dNdr: [[T; 2]; 3] = [
        [-one, -one],
        [one, zero],
        [zero, one]];
    for ino in 0..3 {
        for idim in 0..3 {
            dw[ino][idim] = Area * (
                S2[0] * gd[0][idim] * dNdr[ino][0]
                    + S2[2] * gd[0][idim] * dNdr[ino][1]
                    + S2[2] * gd[1][idim] * dNdr[ino][0]
                    + S2[1] * gd[1][idim] * dNdr[ino][1]);
        }
    }

    let S2p: [T; 3] = [S2[0], S2[1], S2[2]];
    //MakePositiveDefinite_Sim22(S2, S3);

    // compute second derivative
    for ino in 0..3 {
        for jno in 0..3 {
            for idim in 0..3 {
                for jdim in 0..3 {
                    let mut dtmp0: T = zero;
                    dtmp0 += gd[0][idim] * dNdr[ino][0] * cons2[0][0] * gd[0][jdim] * dNdr[jno][0];
                    dtmp0 += gd[0][idim] * dNdr[ino][0] * cons2[0][1] * gd[1][jdim] * dNdr[jno][1];
                    dtmp0 += gd[0][idim] * dNdr[ino][0] * cons2[0][2] * gd[0][jdim] * dNdr[jno][1];
                    dtmp0 += gd[0][idim] * dNdr[ino][0] * cons2[0][2] * gd[1][jdim] * dNdr[jno][0];
                    dtmp0 += gd[1][idim] * dNdr[ino][1] * cons2[1][0] * gd[0][jdim] * dNdr[jno][0];
                    dtmp0 += gd[1][idim] * dNdr[ino][1] * cons2[1][1] * gd[1][jdim] * dNdr[jno][1];
                    dtmp0 += gd[1][idim] * dNdr[ino][1] * cons2[1][2] * gd[0][jdim] * dNdr[jno][1];
                    dtmp0 += gd[1][idim] * dNdr[ino][1] * cons2[1][2] * gd[1][jdim] * dNdr[jno][0];
                    dtmp0 += gd[0][idim] * dNdr[ino][1] * cons2[2][0] * gd[0][jdim] * dNdr[jno][0];
                    dtmp0 += gd[0][idim] * dNdr[ino][1] * cons2[2][1] * gd[1][jdim] * dNdr[jno][1];
                    dtmp0 += gd[0][idim] * dNdr[ino][1] * cons2[2][2] * gd[0][jdim] * dNdr[jno][1];
                    dtmp0 += gd[0][idim] * dNdr[ino][1] * cons2[2][2] * gd[1][jdim] * dNdr[jno][0];
                    dtmp0 += gd[1][idim] * dNdr[ino][0] * cons2[2][0] * gd[0][jdim] * dNdr[jno][0];
                    dtmp0 += gd[1][idim] * dNdr[ino][0] * cons2[2][1] * gd[1][jdim] * dNdr[jno][1];
                    dtmp0 += gd[1][idim] * dNdr[ino][0] * cons2[2][2] * gd[0][jdim] * dNdr[jno][1];
                    dtmp0 += gd[1][idim] * dNdr[ino][0] * cons2[2][2] * gd[1][jdim] * dNdr[jno][0];
                    ddw[ino][jno][idim][jdim] = dtmp0 * Area;
                }
            }
            let dtmp1 = Area *
                (S2p[0] * dNdr[ino][0] * dNdr[jno][0]
                    + S2p[2] * dNdr[ino][0] * dNdr[jno][1]
                    + S2p[2] * dNdr[ino][1] * dNdr[jno][0]
                    + S2p[1] * dNdr[ino][1] * dNdr[jno][1]);
            ddw[ino][jno][0][0] += dtmp1;
            ddw[ino][jno][1][1] += dtmp1;
            ddw[ino][jno][2][2] += dtmp1;
        }
    }
    w
}

#[test]
fn test_wdwddw_cst() {
    let pos0 = [[1.2, 2.1, 3.4], [3.5, 5.2, 4.3], [3.4, 4.8, 2.4]];
    let pos1 = [[3.1, 2.2, 1.5], [4.3, 3.6, 2.0], [5.2, 4.5, 3.4]];
    let mut dw0 = [[0_f64; 3]; 3];
    let mut ddw0 = [[[[0_f64; 3]; 3]; 3]; 3];
    let lambda = 1.3;
    let myu = 1.9;
    let w0 = wdwddw_cst(&mut dw0, &mut ddw0,
                        pos0, pos1, lambda, myu);
    let eps = 1.0e-5_f64;
    for ino in 0..3 {
        for idim in 0..3 {
            let mut pos1a = pos1.clone();
            pos1a[ino][idim] += eps;
            let mut dw1 = [[0_f64; 3]; 3];
            let mut ddw1 = [[[[0_f64; 3]; 3]; 3]; 3];
            let w1 = wdwddw_cst(&mut dw1, &mut ddw1,
                                pos0, pos1a, lambda, myu);
            let dw_numerical = (w1 - w0) / eps;
            let dw_analytical = dw0[ino][idim];
            assert!( (dw_numerical-dw_analytical).abs() < 1.0e-4 );
            for jno in 0..3 {
                for jdim in 0..3 {
                    let ddw_numerical = (dw1[jno][jdim] - dw0[jno][jdim])/eps;
                    let ddw_analytical = ddw0[jno][ino][jdim][idim];
                    assert!( (ddw_numerical-ddw_analytical).abs() < 1.0e-4 );
                }
            }
        }
    }
}
