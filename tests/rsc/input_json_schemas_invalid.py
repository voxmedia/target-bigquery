schema_nested_2_invalid_JSON = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {
      "column_name_missing_quotes: {
        "type": [
          "null",
          "integer"
        ]
      } }
  },
  "key_properties": [
    "Id"
  ]
}
"""


invalild_schema_top_field_empty_props = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {

      "Languages": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "string": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": "string"
            }
          }
        }
      },


      "Languages_Empty_Properties": {
        "type": [
          "null",
          "object"
        ],
        "properties": {

        }
      }

    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalild_schema_top_field_empty_type = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {

      "Languages": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "string": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": "string"
            }
          }
        }
      },

      "BudgetId_empty_type": {
        "type": [
        ]
      }

    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalid_schema_subfield_empty_props = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {

      "ForwardCompatibilityMap": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "KeyValuePairOfstringstring": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        }
      },
      "ForwardCompatibilityMap_subfield_empty_props": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "KeyValuePairOfstringstring": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "properties": {
                  }
                }
              }
            }
          }
        }
      }

    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalid_schema_subfield_empty_type = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {

      "ForwardCompatibilityMap": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "KeyValuePairOfstringstring": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        }
      },
      "ForwardCompatibilityMap_subfield_empty_type": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "KeyValuePairOfstringstring": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                  ]
                }
              }
            }
          }
        }
      }

    }
  },
  "key_properties": [
    "Id"
  ]
}"""


# this schema is based on this issue: https://github.com/adswerve/target-bigquery/issues/3
invalid_schema_under_anyOf_empty_props_example_1 = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {


"sample_column_anyOf_empty_properties": {
  "anyOf": [
    {
      "items": {
        "properties": {
          "name": { "type": [ "null", "string" ] },
          "value": { "type": [ "null", "string" ] }
        },
        "type": [ "null", "object" ]
      },
      "type": [ "null", "array" ]
    },
    {
      "properties": {},
      "type": ["null", "object"]
    }
  ]
},
        "ForwardCompatibilityMap": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "KeyValuePairOfstringstring": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        }
      }

    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalid_schema_under_anyOf_empty_props_example_2 = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {


      "AudienceAdsBidAdjustment": {
        "type": [
          "null",
          "integer"
        ]
      },
      "BiddingScheme_missing_props_item_10": {
        "anyOf": [
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "InheritedBidStrategyType": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              },
              "TargetCpa": {
                "type": [
                  "null",
                  "number"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "TargetRoas": {
                "type": [
                  "null",
                  "number"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              },
              "TargetRoas": {
                "type": [
                  "null",
                  "number"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              },
              "TargetAdPosition": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "TargetImpressionShare": {
                "type": [
                  "null",
                  "number"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
            }
          }
        ]
      }
    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalid_schema_under_anyOf_deep_nested_empty_props = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {




      "Settings": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "Setting": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "anyOf": [
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Details": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "TargetSettingDetail": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": [
                              "null",
                              "object"
                            ],
                            "additionalProperties": false,
                            "properties": {
                              "CriterionTypeGroup": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "TargetAndBid": {
                                "type": [
                                  "boolean"
                                ]
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "LocalInventoryAdsEnabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "Priority": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "SalesCountryCode": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "StoreId": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "BidBoostValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidMaxValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidOption": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "DomainName": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Language": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "PageFeedIds": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "long": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": "integer"
                          }
                        }
                      }
                    },
                    "Source": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
      },


      "Settings_nested_anyof_missing_type_properties": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "Setting": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "anyOf": [
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Details": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "TargetSettingDetail": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": [
                              "null",
                              "object"
                            ],
                            "additionalProperties": false,
                            "properties": {
                              "CriterionTypeGroup": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "TargetAndBid_missing_type_properties": {

                                "properties": {}
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "LocalInventoryAdsEnabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "Priority": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "SalesCountryCode": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "StoreId": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "BidBoostValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidMaxValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidOption": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "DomainName": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Language": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "PageFeedIds": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "long": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": "integer"
                          }
                        }
                      }
                    },
                    "Source": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
      }
    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalid_schema_under_anyOf_deep_nested_empty_type = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {




      "Settings": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "Setting": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "anyOf": [
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Details": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "TargetSettingDetail": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": [
                              "null",
                              "object"
                            ],
                            "additionalProperties": false,
                            "properties": {
                              "CriterionTypeGroup": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "TargetAndBid": {
                                "type": [
                                  "boolean"
                                ]
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "LocalInventoryAdsEnabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "Priority": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "SalesCountryCode": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "StoreId": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "BidBoostValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidMaxValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidOption": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "DomainName": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Language": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "PageFeedIds": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "long": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": "integer"
                          }
                        }
                      }
                    },
                    "Source": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
      },


      "Settings_nested_anyof_missing_type_properties": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "Setting": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "anyOf": [
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Details": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "TargetSettingDetail": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": [
                              "null",
                              "object"
                            ],
                            "additionalProperties": false,
                            "properties": {
                              "CriterionTypeGroup": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "TargetAndBid_missing_type_properties": {
                                "type": [
                                ]
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "LocalInventoryAdsEnabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "Priority": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "SalesCountryCode": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "StoreId": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "BidBoostValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidMaxValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidOption": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "DomainName": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Language": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "PageFeedIds": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "long": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": "integer"
                          }
                        }
                      }
                    },
                    "Source": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
      }
    }
  },
  "key_properties": [
    "Id"
  ]
}"""



invalid_schema_anyOf_discount_codes_empty_type = """{
    "type": "SCHEMA",
    "stream": "nested_stream",
    "schema": {
        "properties": {

            "discount_codes": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "amount": {
                                    "type": [
                                    ]
                                },
                                "code": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "type": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            }

        },
        "type": [
            "null",
            "object"
        ]
    },
    "key_properties": [
        "campaign_id",
        "adset_id",
        "ad_id",
        "date_start",
        "age",
        "gender"
    ],
    "bookmark_properties": [
        "date_start"
    ]
}"""


invalid_schema_anyOf_tax_lines_empty_type = """{
  "type": "SCHEMA",
  "stream": "nested_stream",
  "schema": {
    "properties": {

      "tax_lines": {
        "anyOf": [
          {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "price": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "title": {
                  "type": [
                  ]
                }
              }
            }
          },
          {
            "type": "null"
          }
        ]
      }



    },
    "type": [
      "null",
      "object"
    ]
  },
  "key_properties": [
    "campaign_id",
    "adset_id",
    "ad_id",
    "date_start",
    "age",
    "gender"
  ],
  "bookmark_properties": [
    "date_start"
  ]
}"""


# can't parse this one
invalid_schema_anyOf_line_items_empty_props = """{
    "type": "SCHEMA",
    "stream": "nested_stream",
    "schema": {
        "properties": {

            "line_items": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "grams": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "images": {
                                    "type": [
                                        "null",
                                        "object"
                                    ],
                                    "additionalProperties": false,
                                    "properties": {
                                        "large": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "medium": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "original": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "small": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        }
                                    }
                                },
                                "price": {
                                    "type": [
                                        "null",
                                        "number"
                                    ],
                                    "multipleOf": 1e-08
                                },
                                "properties": {
                                    "anyOf": [
                                        {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "additionalProperties": false,
                                                "properties": {
                                                    
                                                   
                                                }
                                            }
                                        },
                                        {
                                            "type": "null"
                                        }
                                    ]
                                },
                                "quantity": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "shopify_product_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "shopify_variant_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "sku": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "subscription_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "variant_title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "vendor": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            }
        },
        "type": [
            "null",
            "object"
        ]
    },
    "key_properties": [
        "campaign_id",
        "adset_id",
        "ad_id",
        "date_start",
        "age",
        "gender"
    ],
    "bookmark_properties": [
        "date_start"
    ]
}"""



invalid_schema_anyOf_line_items_empty_type = """{
    "type": "SCHEMA",
    "stream": "nested_stream",
    "schema": {
        "properties": {

            "line_items": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "grams": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "images": {
                                    "type": [
                                        "null",
                                        "object"
                                    ],
                                    "additionalProperties": false,
                                    "properties": {
                                        "large": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "medium": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "original": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "small": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        }
                                    }
                                },
                                "price": {
                                    "type": [
                                        "null",
                                        "number"
                                    ],
                                    "multipleOf": 1e-08
                                },
                                "properties": {
                                    "anyOf": [
                                        {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "additionalProperties": false,
                                                "properties": {
                                                    "name": {
                                                        "type": [
                                                            "null",
                                                            "string"
                                                        ]
                                                    },
                                                    "value": {
                                                        "type": [
                                                        ]
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "type": "null"
                                        }
                                    ]
                                },
                                "quantity": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "shopify_product_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "shopify_variant_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "sku": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "subscription_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "variant_title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "vendor": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            }
        },
        "type": [
            "null",
            "object"
        ]
    },
    "key_properties": [
        "campaign_id",
        "adset_id",
        "ad_id",
        "date_start",
        "age",
        "gender"
    ],
    "bookmark_properties": [
        "date_start"
    ]
}"""


invalid_salesforce_schema = """{"type": "SCHEMA", "stream": "Salesforce_CaseHistory", "schema": {"type": "object", "additionalProperties": false, "properties": {"Id": {"type": "string"}, "IsDeleted": {"type": ["null", "boolean"]}, "CaseId": {"type": ["null", "string"]}, "CreatedById": {"type": ["null", "string"]}, "CreatedDate": {"anyOf": [{"type": "string", "format": "date-time"}, {"type": ["string", "null"]}]}, "Field": {"type": ["null", "string"]}, "OldValue": {}, "NewValue": {}}}, "key_properties": ["Id"]}"""

# Bing Ads accounts

"""
This is invalid schema

Invalid part:
"KeyValueOfstringbase":{"type":["null","array"],"items":"KeyValueOfstringbase"}

This table has KeyValueOfstringbase column.
It previously created an issue, while using method 1 of schema conversion.

We figured out how to solve the problem in Bing Ads column KeyValueOfstringbase, aka KeyValuePairOfstringbase, aka KeyValuePairOfstringbase64Binary (it got renamed).

Schema conversion (JSON → BigQuery) was failing, because tap-bing-ads was generating incorrect schema for this column.

Solution:

Replace:
pip install tap-bing-ads==2.0.15
with
pip install tap-bing-ads==2.0.16

I tested, all data gets loaded successfully, including the problem column

"""

bing_ads_accounts_invalid = '{"type":"SCHEMA","stream":"accounts","schema":{"type":["null","object"],"additionalProperties":false,"properties":{"BillToCustomerId":{"type":["null","integer"]},"CurrencyCode":{"type":["null","string"]},"AccountFinancialStatus":{"type":["null","string"]},"Id":{"type":["null","integer"]},"Language":{"type":["null","string"]},"LastModifiedByUserId":{"type":["null","integer"]},"LastModifiedTime":{"type":["null","string"],"format":"date-time"},"Name":{"type":["null","string"]},"Number":{"type":["null","string"]},"ParentCustomerId":{"type":["integer"]},"PaymentMethodId":{"type":["null","integer"]},"PaymentMethodType":{"type":["null","string"]},"PrimaryUserId":{"type":["null","integer"]},"AccountLifeCycleStatus":{"type":["null","string"]},"TimeStamp":{"type":["null","string"]},"TimeZone":{"type":["null","string"]},"PauseReason":{"type":["null","integer"]},"ForwardCompatibilityMap":{"type":["null","object"],"properties":{"KeyValuePairOfstringstring":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"key":{"type":["null","string"]},"value":{"type":["null","string"]}}}}}},"LinkedAgencies":{"type":["null","object"],"properties":{"CustomerInfo":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"Id":{"type":["null","integer"]},"Name":{"type":["null","string"]}}}}}},"SalesHouseCustomerId":{"type":["null","integer"]},"TaxInformation":{"type":["null","object"],"properties":{"KeyValuePairOfstringstring":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"key":{"type":["null","string"]},"value":{"type":["null","string"]}}}}}},"BackUpPaymentInstrumentId":{"type":["null","integer"]},"BillingThresholdAmount":{"type":["null","number"]},"BusinessAddress":{"type":["null","object"],"additionalProperties":false,"properties":{"City":{"type":["null","string"]},"CountryCode":{"type":["null","string"]},"Id":{"type":["null","integer"]},"Line1":{"type":["null","string"]},"Line2":{"type":["null","string"]},"Line3":{"type":["null","string"]},"Line4":{"type":["null","string"]},"PostalCode":{"type":["null","string"]},"StateOrProvince":{"type":["null","string"]},"TimeStamp":{"type":["null","string"]},"BusinessName":{"type":["null","string"]}}},"AutoTagType":{"type":["null","string"]},"SoldToPaymentInstrumentId":{"type":["null","integer"]},"TaxCertificate":{"type":["null","object"],"additionalProperties":false,"properties":{"TaxCertificateBlobContainerName":{"type":["null","string"]},"TaxCertificates":{"type":["null","object"],"properties":{"KeyValueOfstringbase":{"type":["null","array"],"items":"KeyValueOfstringbase"}}},"Status":{"type":["null","string"]}}}}},"key_properties":[]}'


# this schema is invalid, it has "properties":{}
shopify_abandoned_checkouts_malformed = """{"type":"SCHEMA",
      "stream": "abandoned_checkouts",
      "tap_stream_id": "abandoned_checkouts",
      "schema": {
        "type": "object",
        "properties": {
          "note_attributes": {
            "items": {
              "properties": {
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "location_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "buyer_accepts_marketing": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "currency": {
            "type": [
              "null",
              "string"
            ]
          },
          "completed_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "token": {
            "type": [
              "null",
              "string"
            ]
          },
          "billing_address": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
              "phone": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "country": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "first_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "latitude": {
                "type": [
                  "null",
                  "number"
                ]
              },
              "zip": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "last_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "address2": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "address1": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "country_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "city": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "company": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "longitude": {
                "type": [
                  "null",
                  "number"
                ]
              }
            }
          },
          "email": {
            "type": [
              "null",
              "string"
            ]
          },
          "discount_codes": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "amount": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "code": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "customer_locale": {
            "type": [
              "null",
              "string"
            ]
          },
          "created_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "updated_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "gateway": {
            "type": [
              "null",
              "string"
            ]
          },
          "referring_site": {
            "type": [
              "null",
              "string"
            ]
          },
          "source_identifier": {
            "type": [
              "null",
              "string"
            ]
          },
          "total_weight": {
            "type": [
              "null",
              "integer"
            ]
          },
          "tax_lines": {
            "items": {
              "properties": {
                "price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "rate": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "compare_at": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "position": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "source": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "zone": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "total_line_items_price": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "closed_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "device_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "phone": {
            "type": [
              "null",
              "string"
            ]
          },
          "source_name": {
            "type": [
              "null",
              "string"
            ]
          },
          "id": {
            "type": [
              "null",
              "string"
            ]
          },
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "total_tax": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "subtotal_price": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "line_items": {
            "items": {
              "properties": {
                "applied_discounts": {
                  "type": [
                    "null",
                    "array"
                  ],
                  "items": {
                    "properties": {
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "code": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "savings": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "type": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  }
                },
                "total_discount_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "pre_tax_price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "grams": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "compare_at_price": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "destination_location_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "line_price": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "origin_location_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "applied_discount": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "fulfillable_quantity": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "variant_title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "properties": {
                  "anyOf": [
                    {
                      "items": {
                        "properties": {
                          "name": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "value": {
                            "type": [
                              "null",
                              "string"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "type": [
                        "null",
                        "array"
                      ]
                    },
                    {
                      "properties": {},
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  ]
                },
                "tax_code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "discount_allocations": {
                  "items": {
                    "properties": {
                      "discount_application_index": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "amount_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                          "type": [
                              "null",
                              "object"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "admin_graphql_api_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "pre_tax_price": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "sku": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "product_exists": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "total_discount": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "fulfillment_status": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "gift_card": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "taxable": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "vendor": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "tax_lines": {
                  "items": {
                    "properties": {
                      "price_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "price": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "rate": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "compare_at": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "position": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "source": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "zone": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "origin_location": {
                  "properties": {
                    "country_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address1": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "city": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address2": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "zip": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "requires_shipping": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "fulfillment_service": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "variant_inventory_management": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "destination_location": {
                  "properties": {
                    "country_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address1": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "city": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address2": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "zip": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "quantity": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "product_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "variant_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "source_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "total_discounts": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "note": {
            "type": [
              "null",
              "string"
            ]
          },
          "presentment_currency": {
            "type": [
              "null",
              "string"
            ]
          },
          "shipping_lines": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "applied_discounts": {
                  "type": [
                    "null",
                    "array"
                  ],
                  "items": {
                    "properties": {
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "code": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "savings": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "type": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  }
                },
                "custom_tax_lines": {
                  "items": {
                    "properties": {
                      "price": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "rate": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "compare_at": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "position": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "source": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "zone": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "phone": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "validation_context": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "carrier_identifier": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "api_client_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "price": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "requested_fulfillment_service_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "tax_lines": {
                  "items": {
                    "properties": {
                      "price_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "price": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "rate": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "compare_at": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "position": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "source": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "zone": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "carrier_service_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "delivery_category": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "markup": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "source": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          },
          "user_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "source": {
            "type": [
              "null",
              "string"
            ]
          },
          "shipping_address": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
              "phone": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "country": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "first_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "latitude": {
                "type": [
                  "null",
                  "number"
                ]
              },
              "zip": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "last_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "address2": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "address1": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "country_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "city": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "company": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "longitude": {
                "type": [
                  "null",
                  "number"
                ]
              }
            }
          },
          "abandoned_checkout_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "landing_site": {
            "type": [
              "null",
              "string"
            ]
          },
          "customer": {
            "type": "object",
            "properties": {
              "last_order_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "currency": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "email": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "multipass_identifier": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "default_address": {
                "type": [
                  "null",
                  "object"
                ],
                "properties": {
                  "city": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "address1": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "zip": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "id": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "country_name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "province": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "phone": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "country": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "first_name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "customer_id": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "default": {
                    "type": [
                      "null",
                      "boolean"
                    ]
                  },
                  "last_name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "country_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "province_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "address2": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "company": {
                    "type": [
                      "null",
                      "string"
                    ]
                  }
                }
              },
              "orders_count": {
                "type": [
                  "null",
                  "integer"
                ]
              },
              "state": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "verified_email": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "total_spent": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "last_order_id": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "first_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "updated_at": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              },
              "note": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "phone": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "admin_graphql_api_id": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "addresses": {
                "type": [
                  "null",
                  "array"
                ],
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "properties": {
                    "city": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address1": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "zip": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "country_name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "phone": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "country": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "first_name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "customer_id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "default": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "last_name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "country_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address2": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "company": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              },
              "last_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "tags": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "tax_exempt": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "id": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "accepts_marketing": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "accepts_marketing_updated_at": {
                "anyOf": [
                  {
                    "type": "string",
                    "format": "date-time"
                  },
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              },
              "created_at": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              }
            }
          },
          "total_price": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "cart_token": {
            "type": [
              "null",
              "string"
            ]
          },
          "taxes_included": {
            "type": [
              "null",
              "boolean"
            ]
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "id"
            ],
            "forced-replication-method": "INCREMENTAL",
            "valid-replication-keys": [
              "updated_at"
            ],
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "note_attributes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "location_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "buyer_accepts_marketing"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "currency"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "completed_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "token"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "billing_address"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "email"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "discount_codes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "customer_locale"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "updated_at"
          ],
          "metadata": {
            "inclusion": "automatic"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gateway"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "referring_site"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source_identifier"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_weight"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "tax_lines"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_line_items_price"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "closed_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "device_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "phone"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source_name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_tax"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "subtotal_price"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "line_items"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source_url"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_discounts"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "note"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "presentment_currency"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "shipping_lines"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "user_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "shipping_address"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "abandoned_checkout_url"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "landing_site"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "customer"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_price"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "cart_token"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "taxes_included"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "id"
      ],
      "replication_key": "updated_at",
      "replication_method": "INCREMENTAL"
    }"""

