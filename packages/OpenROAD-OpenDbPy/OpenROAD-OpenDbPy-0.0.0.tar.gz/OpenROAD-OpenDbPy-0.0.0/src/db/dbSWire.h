///////////////////////////////////////////////////////////////////////////////
// BSD 3-Clause License
//
// Copyright (c) 2019, Nefelus Inc
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// * Redistributions of source code must retain the above copyright notice, this
//   list of conditions and the following disclaimer.
//
// * Redistributions in binary form must reproduce the above copyright notice,
//   this list of conditions and the following disclaimer in the documentation
//   and/or other materials provided with the distribution.
//
// * Neither the name of the copyright holder nor the names of its
//   contributors may be used to endorse or promote products derived from
//   this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.

#pragma once

#include "dbCore.h"
#include "dbId.h"
#include "dbTypes.h"
#include "odb.h"

namespace odb {

class _dbSWire;
class _dbNet;
class _dbSBox;
class dbDiff;

struct _dbSWireFlags
{
  dbWireType::Value _wire_type : 6;
  uint _spare_bits : 26;
};

class _dbSWire : public _dbObject
{
 public:
  _dbSWireFlags _flags;
  dbId<_dbNet> _net;
  dbId<_dbNet> _shield;
  dbId<_dbSBox> _wires;
  dbId<_dbSWire> _next_swire;

  _dbSWire(_dbDatabase*)
  {
    _flags._wire_type = dbWireType::NONE;
    _flags._spare_bits = 0;
  }

  _dbSWire(_dbDatabase*, const _dbSWire& s)
      : _flags(s._flags),
        _net(s._net),
        _shield(s._shield),
        _wires(s._wires),
        _next_swire(s._next_swire)
  {
  }

  ~_dbSWire() {}

  void addSBox(_dbSBox* box);
  void removeSBox(_dbSBox* box);

  bool operator==(const _dbSWire& rhs) const;
  bool operator!=(const _dbSWire& rhs) const { return !operator==(rhs); }
  bool operator<(const _dbSWire& rhs) const;

  void differences(dbDiff& diff, const char* field, const _dbSWire& rhs) const;
  void out(dbDiff& diff, char side, const char* field) const;
};

inline dbOStream& operator<<(dbOStream& stream, const _dbSWire& wire)
{
  uint* bit_field = (uint*) &wire._flags;
  stream << *bit_field;
  stream << wire._net;
  stream << wire._shield;
  stream << wire._wires;
  stream << wire._next_swire;

  return stream;
}

inline dbIStream& operator>>(dbIStream& stream, _dbSWire& wire)
{
  uint* bit_field = (uint*) &wire._flags;
  stream >> *bit_field;
  stream >> wire._net;
  stream >> wire._shield;
  stream >> wire._wires;
  stream >> wire._next_swire;

  return stream;
}

}  // namespace odb
