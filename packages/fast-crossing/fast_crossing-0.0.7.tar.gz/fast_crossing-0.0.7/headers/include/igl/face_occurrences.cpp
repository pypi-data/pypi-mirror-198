// This file is part of libigl, a simple c++ geometry processing library.
//
// Copyright (C) 2013 Alec Jacobson <alecjacobson@gmail.com>
//
// This Source Code Form is subject to the terms of the Mozilla Public License
// v. 2.0. If a copy of the MPL was not distributed with this file, You can
// obtain one at http://mozilla.org/MPL/2.0/.
#include "face_occurrences.h"
#include "list_to_matrix.h"
#include "matrix_to_list.h"

#include <map>
#include "sort.h"
#include <cassert>

template <typename IntegerF, typename IntegerC>
IGL_INLINE void igl::face_occurrences(
  const std::vector<std::vector<IntegerF> > & F,
  std::vector<IntegerC> & C)
{
  using namespace std;

  // Get a list of sorted faces
  vector<vector<IntegerF> > sortedF = F;
  for(int i = 0; i < (int)F.size();i++)
  {
    sort(sortedF[i].begin(),sortedF[i].end());
  }
  // Count how many times each sorted face occurs
  map<vector<IntegerF>,int> counts;
  for(int i = 0; i < (int)sortedF.size();i++)
  {
    if(counts.find(sortedF[i]) == counts.end())
    {
      // initialize to count of 1
      counts[sortedF[i]] = 1;
    }else
    {
      // increment count
      counts[sortedF[i]]++;
      assert(counts[sortedF[i]] == 2 && "Input should be manifold");
    }
  }

  // Resize output to fit number of ones
  C.resize(F.size());
  for(int i = 0;i< (int)F.size();i++)
  {
    // sorted face should definitely be in counts map
    assert(counts.find(sortedF[i]) != counts.end());
    C[i] = static_cast<IntegerC>(counts[sortedF[i]]);
  }
}

template <typename DerivedF, typename DerivedC>
IGL_INLINE void igl::face_occurrences(
  const Eigen::MatrixBase<DerivedF> & F,
  Eigen::PlainObjectBase<DerivedC> & C)
{
  // Should really just rewrite using Eigen+libigl ...
  std::vector<std::vector<typename DerivedF::Scalar> > vF;
  matrix_to_list(F,vF);
  std::vector<typename DerivedC::Scalar> vC;
  igl::face_occurrences(vF,vC);
  list_to_matrix(vC,C);
}

#ifdef IGL_STATIC_LIBRARY
// Explicit template instantiation
// generated by autoexplicit.sh
template void igl::face_occurrences<unsigned int, int>(std::vector<std::vector<unsigned int, std::allocator<unsigned int> >, std::allocator<std::vector<unsigned int, std::allocator<unsigned int> > > > const&, std::vector<int, std::allocator<int> >&);
template void igl::face_occurrences<int, int>(std::vector<std::vector<int, std::allocator<int> >, std::allocator<std::vector<int, std::allocator<int> > > > const&, std::vector<int, std::allocator<int> >&);
#endif
