use numpy::{IntoPyArray,
            PyReadonlyArray1, PyReadonlyArray2, PyReadonlyArrayDyn,
            PyArray3, PyArray2, PyArray1};
use pyo3::{pymodule, types::PyModule, PyResult, Python, pyfunction, wrap_pyfunction};


pub fn biharmonics(
    tri2vtx: &[usize],
    vtx2xyz: &[f32],
    sample2vtx: &[usize],
    i_sample_fix: usize ) -> Vec<f32>
{  // set pattern to sparse matrix
    let vtx2vtx = del_msh::vtx2vtx::from_uniform_mesh2(
        &tri2vtx, 3, vtx2xyz.len() / 3);
    let mut m = del_ls::sparse_square::Matrix::<f64>::new();
    m.symbolic_initialization(&vtx2vtx.0, &vtx2vtx.1);
    m.set_zero();
    del_misc::mesh_laplacian::merge_trimesh3(
        &mut m,
        &mut vec!(),
        &tri2vtx, &vtx2xyz);
    let m = del_ls::sparse_matrix_multiplication::mult_square_matrices(
        &m, &m);
    let mut ls = del_ls::linearsystem::Solver::<f64>::new();
    ls.sparse = m;
    ls.r_vec = vec!(0_f64; ls.sparse.num_blk);
    let penalty = 1.0e+2;
    for &i_vtx in sample2vtx {
        ls.sparse.row2val[i_vtx] += penalty;
    }
    ls.r_vec[sample2vtx[i_sample_fix]] += penalty;
    ls.ilu.initialize_iluk(&ls.sparse, 3);
// ls.ilu.initialize_full(ls.sparse.num_blk);
    println!("{}", ls.ilu.idx2col.len());
    del_ls::sparse_ilu::copy_value(&mut ls.ilu, &ls.sparse);
    del_ls::sparse_ilu::decompose(&mut ls.ilu);
    //
    ls.conv_ratio_tol = 1.0e-5;
    ls.max_num_iteration = 5000;
    ls.solve_pcg();
    println!("num_iteration for heat: {}", ls.conv.len());
    println!("{:?}", ls.conv.last());
    let vtx2heat = ls.u_vec.clone();
    let vtx2heat = vtx2heat.iter().map(|v| *v as f32).collect();
    vtx2heat
}


/// Formats the sum of two numbers as string.
#[pyfunction]
fn biharmonic<'a>(
    py: Python<'a>,
    tri2vtx: PyReadonlyArray2<'a, usize>,
    vtx2xyz: PyReadonlyArray2<'a, f32>,
    sample2vtx: PyReadonlyArray1<'a, usize>,
    i_sample_fix: usize) -> &'a PyArray1<f32> {
    let vtx2heat = biharmonics(
        tri2vtx.as_slice().unwrap(),
        vtx2xyz.as_slice().unwrap(),
        sample2vtx.as_slice().unwrap(),
        i_sample_fix);
    numpy::ndarray::Array1::from_vec(vtx2heat).into_pyarray(py)
}


/// A Python module implemented in Rust.
#[pymodule]
fn del_misc(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(biharmonic, m)?)?;
    Ok(())
}