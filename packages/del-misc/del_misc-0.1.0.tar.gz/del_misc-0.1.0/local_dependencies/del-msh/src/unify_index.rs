//! unify the index of uv and xyz vertices for Wavefront Obj format

pub fn unify_separate_trimesh_indexing_xyz_uv(
    vtx_xyz2xyz: &[f32],
    vtx_uv2uv: &[f32],
    tri2vtx_xyz: &[usize],
    tri2vtx_uv: &[usize]) -> (Vec<f32>, Vec<f32>, Vec<usize>, Vec<usize>, Vec<usize>)
{
    assert_eq!(tri2vtx_xyz.len(), tri2vtx_uv.len());
    let vtx_xyz2tri = crate::vtx2elem::from_uniform_mesh(
        tri2vtx_xyz, 3, vtx_xyz2xyz.len() / 3);
    let vtx_uv2tri = crate::vtx2elem::from_uniform_mesh(
        tri2vtx_uv, 3, vtx_uv2uv.len() / 2);
    let num_tri = tri2vtx_xyz.len() / 3;
    let mut tri2uni = vec!(usize::MAX; num_tri * 3);
    let mut uni2vtx_uv = Vec::<usize>::new();
    let mut uni2vtx_xyz = Vec::<usize>::new();

    for i_tri in 0..num_tri {
        for i_node in 0..3 {
            let i_vtx_uv = tri2vtx_uv[i_tri * 3 + i_node];
            let s1 = &vtx_uv2tri.1[vtx_uv2tri.0[i_vtx_uv]..vtx_uv2tri.0[i_vtx_uv + 1]];
            for jtri0 in s1.into_iter() {
                let jtri = *jtri0;
                let jno = crate::tri2vtx::find_index_tri(&tri2vtx_uv[jtri*3..jtri*3+3], i_vtx_uv);
                assert_eq!(tri2vtx_uv[jtri * 3 + jno], i_vtx_uv);
            }
        }
    }

    for i_tri in 0..num_tri {
        for i_node in 0..3 {
            if tri2uni[i_tri * 3 + i_node] != usize::MAX { continue; }
            let i_vtx_xyz = tri2vtx_xyz[i_tri * 3 + i_node];
            let i_vtx_uv = tri2vtx_uv[i_tri * 3 + i_node];
            let s0 = &vtx_xyz2tri.1[vtx_xyz2tri.0[i_vtx_xyz]..vtx_xyz2tri.0[i_vtx_xyz + 1]];
            let s1 = &vtx_uv2tri.1[vtx_uv2tri.0[i_vtx_uv]..vtx_uv2tri.0[i_vtx_uv + 1]];
            let s0 = std::collections::BTreeSet::<&usize>::from_iter(s0.iter());
            let s1 = std::collections::BTreeSet::<&usize>::from_iter(s1.iter());
            let intersection: Vec<_> = s0.intersection(&s1).collect();
            if intersection.is_empty() { continue; }
            let i_uni = uni2vtx_uv.len(); // new unified vertex
            assert_eq!(uni2vtx_uv.len(), uni2vtx_xyz.len());
            uni2vtx_xyz.push(i_vtx_xyz);
            uni2vtx_uv.push(i_vtx_uv);
            for j_tri in intersection.into_iter().cloned() {
                let j_node_xyz = crate::tri2vtx::find_index_tri(&tri2vtx_xyz[j_tri *3..j_tri *3+3], i_vtx_xyz);
                assert_eq!(tri2vtx_xyz[j_tri * 3 + j_node_xyz], i_vtx_xyz);
                let j_node_uv = crate::tri2vtx::find_index_tri(&tri2vtx_uv[j_tri *3..j_tri *3+3], i_vtx_uv);
                assert_eq!(tri2vtx_uv[j_tri * 3 + j_node_uv], i_vtx_uv);
                if j_node_xyz != j_node_uv {  // this sometime happens
                    continue;
                }
                assert_eq!(tri2uni[j_tri * 3 + j_node_xyz], usize::MAX);
                tri2uni[j_tri * 3 + j_node_xyz] = i_uni;
            }
        }
    }
    let num_uni = uni2vtx_xyz.len();
    let mut uni2xyz = vec!(0_f32; num_uni * 3);
    for i_uni in 0..num_uni {
        let ivtx_xyz = uni2vtx_xyz[i_uni];
        uni2xyz[i_uni * 3 + 0] = vtx_xyz2xyz[ivtx_xyz * 3 + 0];
        uni2xyz[i_uni * 3 + 1] = vtx_xyz2xyz[ivtx_xyz * 3 + 1];
        uni2xyz[i_uni * 3 + 2] = vtx_xyz2xyz[ivtx_xyz * 3 + 2];
    }
    let mut uni2uv = vec!(0_f32; num_uni * 2);
    for i_uni in 0..num_uni {
        let i_vtx_uv = uni2vtx_uv[i_uni];
        uni2uv[i_uni * 2 + 0] = vtx_uv2uv[i_vtx_uv * 2 + 0];
        uni2uv[i_uni * 2 + 1] = vtx_uv2uv[i_vtx_uv * 2 + 1];
    }
    (uni2xyz, uni2uv, tri2uni, uni2vtx_xyz, uni2vtx_uv)
}