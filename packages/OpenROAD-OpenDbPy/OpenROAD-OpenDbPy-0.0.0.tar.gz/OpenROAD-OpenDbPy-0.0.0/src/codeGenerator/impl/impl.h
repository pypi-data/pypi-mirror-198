///////////////////////////////////////////////////////////////////////////////
// BSD 3-Clause License
//
// Copyright (c) 2022, The Regents of the University of California
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

//Generator Code Begin Header
#pragma once

#include "odb.h"
#include "dbCore.h"

{% for include in klass.h_includes %}
  #include "{{include}}"
{% endfor %}
// User Code Begin Includes
// User Code End Includes

namespace odb {
  
  
  class dbIStream;
  class dbOStream;
  class dbDiff;
  class _dbDatabase;
  {% for _class in klass.classes %}
    {% if _class in ["dbTable", "dbHashTable"] %}
      template <class T>
    {% endif %}
    class {{ _class }};
  {% endfor %}
  //User Code Begin Classes
  //User Code End Classes

  {% for _struct in klass.structs %}
    {% if not _struct.public %}
    struct {{ _struct.name }}
    {
      {% for field in _struct.fields %}
        {{field.type}} {{field.name}}{% if "bits" in field %} : {{field.bits}}{% endif %}{% if "default" in field %} = {{field.default}}{% endif %};{% if "comment" in field %} {{field.comment}}{% endif %}
      
      {% endfor %}
    };
    {% endif %}
  {% endfor %}
  // User Code Begin Structs
  // User Code End Structs


  class _{{klass.name}} : public _dbObject
  {
    public:
    {% for _enum in klass.enums %}
      {% if not _enum.public %}
        enum {{_enum.name}}{%if type in _enum%} : _enum.type{% endif %}
        {
          {% for value in _enum["values"] %}
            {% if not loop.first %},{% endif %}{{value}}
          {% endfor %}
        };
      {% endif %}
    {% endfor %}
    // User Code Begin Enums
    // User Code End Enums
        
    {% for field in klass.fields %}
      {% if field.table %} 
        dbTable<_{{field.type}}>* {{field.name}}; 
      {% else %}
      {{field.type}} {{field.name}};{% if "comment" in field %} {{field.comment}}{% endif %}

      {% endif %}
    {% endfor %}

    // User Code Begin Fields
    // User Code End Fields
    _{{klass.name}}(_dbDatabase*, const _{{klass.name}}& r);
    _{{klass.name}}(_dbDatabase*);
    {% for constructor in klass.constructors %}
      _{{klass.name}}(_dbDatabase*{% for arg in constructor.args %},{{arg.type}}{% endfor %});
    {% endfor %}
    ~_{{klass.name}}();
    bool operator==(const _{{klass.name}}& rhs) const;
    bool operator!=(const _{{klass.name}}& rhs) const { return !operator==(rhs); }
    bool operator<(const _{{klass.name}}& rhs) const;
    void differences(dbDiff& diff, const char* field, const _{{klass.name}}& rhs) const;
    void out(dbDiff& diff, char side, const char* field) const;
    {% if klass.hasTables %}
    dbObjectTable* getObjectTable(dbObjectType type);
    {% endif %}
    // User Code Begin Methods
    // User Code End Methods
  };
dbIStream& operator>>(dbIStream& stream, _{{klass.name}}& obj);
dbOStream& operator<<(dbOStream& stream, const _{{klass.name}}& obj);
// User Code Begin General
// User Code End General
}
//Generator Code End Header
