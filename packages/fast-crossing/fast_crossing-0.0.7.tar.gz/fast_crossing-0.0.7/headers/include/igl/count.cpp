// This file is part of libigl, a simple c++ geometry processing library.
// 
// Copyright (C) 2016 Alec Jacobson <alecjacobson@gmail.com>
// 
// This Source Code Form is subject to the terms of the Mozilla Public License 
// v. 2.0. If a copy of the MPL was not distributed with this file, You can 
// obtain one at http://mozilla.org/MPL/2.0/.
#include "count.h"
#include "redux.h"

template <typename XType, typename SType>
IGL_INLINE void igl::count(
  const Eigen::SparseMatrix<XType>& X, 
  const int dim,
  Eigen::SparseVector<SType>& S)
{
  // dim must be 2 or 1
  assert(dim == 1 || dim == 2);
  // Get size of input
  int m = X.rows();
  int n = X.cols();
  // resize output
  if(dim==1)
  {
    S = Eigen::SparseVector<SType>(n);
  }else
  {
    S = Eigen::SparseVector<SType>(m);
  }

  // Iterate over outside
  for(int k=0; k<X.outerSize(); ++k)
  {
    // Iterate over inside
    for(typename Eigen::SparseMatrix<XType>::InnerIterator it (X,k); it; ++it)
    {
      if(dim == 1)
      {
        S.coeffRef(it.col()) += (it.value() == 0? 0: 1);
      }else
      {
        S.coeffRef(it.row()) += (it.value() == 0? 0: 1);
      }
    }
  }

}

template <typename AType, typename DerivedB>
IGL_INLINE void igl::count(
  const Eigen::SparseMatrix<AType>& A, 
  const int dim,
  Eigen::PlainObjectBase<DerivedB>& B)
{
  typedef typename DerivedB::Scalar Scalar;
  igl::redux(A,dim,[](Scalar a, Scalar b){ return a+(b==0?0:1);},B);
}

#ifdef IGL_STATIC_LIBRARY
// Explicit template instantiation
// generated by autoexplicit.sh
template void igl::count<bool, Eigen::Matrix<int, -1, 1, 0, -1, 1> >(Eigen::SparseMatrix<bool, 0, int> const&, int, Eigen::PlainObjectBase<Eigen::Matrix<int, -1, 1, 0, -1, 1> >&);
// generated by autoexplicit.sh
template void igl::count<bool, Eigen::Array<int, -1, 1, 0, -1, 1> >(Eigen::SparseMatrix<bool, 0, int> const&, int, Eigen::PlainObjectBase<Eigen::Array<int, -1, 1, 0, -1, 1> >&);
#endif
