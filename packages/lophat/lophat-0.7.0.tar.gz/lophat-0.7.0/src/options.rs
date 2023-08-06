use pyo3::prelude::*;

/// A simple struct for specifying options for R=DV decompositions
///
/// * `maintain_v` - if true, returns full R=DV decomposition,
///   otherwise returns [`RVDecomposition`](crate::RVDecomposition) with field `v` set to `None`.
/// * `n_threads` - number of threads to use in thread pool; ignored by serial algorithms.
///   see [`num_threads`](rayon::ThreadPoolBuilder::num_threads) for more details.
///   Only relevant for lockfree algorithm.
/// * `column_height` - an optional hint to the height of the columns.
///   If `None`, assumed to be `matrix.collect().len()`.
///   All indices must lie in the range `0..column_height`.
///   Only relevant for lockfree algorithm.
/// * `max_chunk_len` - Maximum size of a chunk, given to each thread.
///   Only relevant for lockfree algorithm.
#[pyclass]
#[derive(Clone, Copy)]
pub struct LoPhatOptions {
    #[pyo3(get, set)]
    pub maintain_v: bool,
    #[pyo3(get, set)]
    pub num_threads: usize,
    #[pyo3(get, set)]
    pub column_height: Option<usize>,
    #[pyo3(get, set)]
    pub max_chunk_len: usize,
}

#[pymethods]
impl LoPhatOptions {
    #[new]
    #[pyo3(signature = (maintain_v=false, num_threads=0, column_height=None, max_chunk_len=1))]
    fn new(
        maintain_v: bool,
        num_threads: usize,
        column_height: Option<usize>,
        max_chunk_len: usize,
    ) -> Self {
        LoPhatOptions {
            maintain_v,
            num_threads,
            column_height,
            max_chunk_len,
        }
    }
}

impl Default for LoPhatOptions {
    fn default() -> Self {
        Self {
            maintain_v: false,
            num_threads: 0,
            column_height: None,
            max_chunk_len: 1,
        }
    }
}
