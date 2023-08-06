//! stochastic sampling on mesh

pub fn cumulative_area_sum_condition<F: Fn(usize) -> bool>(
    vtx2xyz: &[f32],
    tri2vtx: &[usize],
    tri2isvalid: F) -> Vec<f32> {
    let mut cumulative_area_sum = vec!();
    let num_tri = tri2vtx.len() / 3;
    assert_eq!(tri2vtx.len(), num_tri * 3);
    cumulative_area_sum.reserve(num_tri + 1);
    cumulative_area_sum.push(0.);
    for idx_tri in 0..num_tri {
        let a0 = if !tri2isvalid(idx_tri) {
            0.0
        } else {
            let i0 = tri2vtx[idx_tri * 3 + 0];
            let i1 = tri2vtx[idx_tri * 3 + 1];
            let i2 = tri2vtx[idx_tri * 3 + 2];
            area3(
                &vtx2xyz[i0 * 3 + 0..i0 * 3 + 3],
                &vtx2xyz[i1 * 3 + 0..i1 * 3 + 3],
                &vtx2xyz[i2 * 3 + 0..i2 * 3 + 3])
        };
        let t0 = cumulative_area_sum[cumulative_area_sum.len() - 1];
        cumulative_area_sum.push(a0 + t0);
    }
    cumulative_area_sum
}


pub fn cumulative_area_sum(
    vtx2xyz: &[f32],
    tri2vtx: &[usize]) -> Vec<f32>
{
    cumulative_area_sum_condition(
        vtx2xyz, tri2vtx, |_itri| { true })
}

pub fn areas_of_triangles_of_mesh(
    tri2vtx: &[usize],
    vtx2xyz: &[f32],) -> Vec<f32>
{
    let num_tri = tri2vtx.len() / 3;
    let mut tri2area = vec!(0_f32; num_tri);
    for idx_tri in 0..num_tri {
        let i0 = tri2vtx[idx_tri * 3 + 0];
        let i1 = tri2vtx[idx_tri * 3 + 1];
        let i2 = tri2vtx[idx_tri * 3 + 2];
        let area = area3(
            &vtx2xyz[i0 * 3 + 0..i0 * 3 + 3],
            &vtx2xyz[i1 * 3 + 0..i1 * 3 + 3],
            &vtx2xyz[i2 * 3 + 0..i2 * 3 + 3]);
        tri2area[idx_tri] = area;
    }
    tri2area
}


pub fn sample_uniform(
    cumulative_area_sum: &[f32],
    val01: f32,
    r1: f32) -> (usize, f32, f32)
{
    let ntri = cumulative_area_sum.len() - 1;
    let a0 = val01 * cumulative_area_sum[ntri];
    let mut itri_l = 0;
    let mut itri_u = ntri;
    loop {  // bisection method
        assert!(cumulative_area_sum[itri_l] < a0);
        assert!(a0 <= cumulative_area_sum[itri_u]);
        let itri_h = (itri_u + itri_l) / 2;
        if itri_u - itri_l == 1 { break; }
        if cumulative_area_sum[itri_h] < a0 {
            itri_l = itri_h;
        } else {
            itri_u = itri_h;
        }
    }
    assert!(cumulative_area_sum[itri_l] < a0);
    assert!(a0 <= cumulative_area_sum[itri_l + 1]);
    let r0 = (a0 - cumulative_area_sum[itri_l]) / (cumulative_area_sum[itri_l + 1] - cumulative_area_sum[itri_l]);
    if r0 + r1 > 1_f32 {
        let r0a = r0;
        let r1a = r1;
        return (itri_l, 1_f32 - r1a, 1_f32 - r0a);
    }
    return (itri_l, r0, r1);
}

pub fn position_on_mesh_tri3(
    itri: usize,
    r0: f32,
    r1: f32,
    vtx2xyz: &[f32],
    tri2vtx: &[usize]) -> [f32; 3] {
    assert!(itri < tri2vtx.len() / 3);
    let i0 = tri2vtx[itri * 3 + 0];
    let i1 = tri2vtx[itri * 3 + 1];
    let i2 = tri2vtx[itri * 3 + 2];
    let p0 = &vtx2xyz[i0 * 3 + 0..i0 * 3 + 3];
    let p1 = &vtx2xyz[i1 * 3 + 0..i1 * 3 + 3];
    let p2 = &vtx2xyz[i2 * 3 + 0..i2 * 3 + 3];
    let r2 = 1_f32 - r0 - r1;
    [
        r0 * p0[0] + r1 * p1[0] + r2 * p2[0],
        r0 * p0[1] + r1 * p1[1] + r2 * p2[1],
        r0 * p0[2] + r1 * p1[2] + r2 * p2[2]]
}

// ---------------------------
// below: private functions

fn area3<T>(p0: &[T], p1: &[T], p2: &[T]) -> T
    where T: num_traits::real::Real + 'static,
          f32: num_traits::AsPrimitive<T>
{
    use num_traits::AsPrimitive;
    assert!(p0.len() == 3 && p1.len() == 3 && p2.len() == 3);
    let v1 = [p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2]];
    let v2 = [p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2]];
    let n = [
        v1[1] * v2[2] - v2[1] * v1[2],
        v1[2] * v2[0] - v2[2] * v1[0],
        v1[0] * v2[1] - v2[0] * v1[1]];
    return (n[0] * n[0] + n[1] * n[1] + n[2] * n[2]).sqrt() * 0.5_f32.as_();
}