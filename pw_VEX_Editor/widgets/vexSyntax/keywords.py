syntax = {
          "comment": ["//"],

          "string": ["\"", "'"],

          "operators": [
                        "!=", "<", ">", "<=", ">=",
                        "\+", "\\-", "\*", "/", "%",
                        "\*", "\+\+", "--", "\*=", "/=", "\|="
                        "\^", "\\|", "&", "\?", ":",
                        "=", ";", "\\", ",", "!"],

          "braces" :['\{', '\}', '\(', '\)', '\[', '\]'],

          "types":[
                   "int",
                   "integer",
                   "float",
                   "vector",
                   "vector2",
                   "vector4",
                   "matrix",
                   "matrix2",
                   "matrix3",
                   "string",
                   "void",
                   "array",
                   "struct",
                   "bsdf",
                   "color",

                   "light",
                   "material",

                   "char",

                   "cvex",
                   "cop",
                   "sop",
                   "pop",
                   "surface",
                   "displace",
                   "fog",
                   "light",
                   "shadow",
                   "chop",
                   "image3d",
          ],
          "keywords":["for",
                      "if",
                      "else",
                      "while",
                      "return",
                      "export",
                      "continue",
                      "break",
                      "do",
                      "foreach",
                      "const",
                     ],
          "directive":["include",
                       "define",
                       "undef",
                       "ifndef",
                       "ifdef",
                       "endif",
                       "else",
                       "if",
                       "elif",
                       "pragma",
                     ],
          "ifdirective":[
                       "defined",
                       "environment",
                       "access",
                       "strcmp",
                     ],
          "pragma":[
                "bindhandle",
                "bindhandlereserved",
                "bindselector",
                "bindselectorreserved",
                "callback",
                "disablewhen",
                "hidewhen",
                "export",
                "group",
                "info",
                "help",
                "hint",
                "inputlabel",
                "label",
                "name",
                "opicon",
                "opmininputs",
                "opmaxinputs",
                "opname",
                "oplabel",
                "opscript",
                "parmhelp",
                "parmtag",
                "ramp",
                "ramp_flt",
                "ramp_rgb",
                "range",
                "rendermask",
                "optable",
                "rename",
          ]

}

