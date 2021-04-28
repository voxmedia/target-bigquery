recharge_addresses = """{
    
    "type": "SCHEMA",
  "stream": "addresses",
    
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "address1": {
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
            "cart_attributes": {
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
            },
            "cart_note": {
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
            "country": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "created_at": {
                "format": "date-time",
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
            "discount_id": {
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
            "id": {
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
            "note_attributes": {
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
            },
            "original_shipping_lines": {
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
            },
            "phone": {
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
            "shipping_lines_override": {
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
            },
            "updated_at": {
                "format": "date-time",
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
        "type": "object",
        "additionalProperties": false
    },
    "stream": "addresses",
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address1"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address2"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "cart_attributes"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "cart_note"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "city"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "company"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "country"
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
                "customer_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "discount_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "first_name"
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
                "last_name"
            ],
            "metadata": {
                "inclusion": "available",
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
                "original_shipping_lines"
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
                "province"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipping_lines_override"
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "zip"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""


recharge_charges = """ {

    "type": "SCHEMA",
    "stream": "charges",
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "address_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "billing_address": {
                "properties": {
                    "address1": {
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
                    "last_name": {
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
                    "province": {
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
                ],
                "additionalProperties": false
            },
            "browser_ip": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "client_details": {
                "properties": {
                    "browser_ip": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "user_agent": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                },
                "type": [
                    "null",
                    "object"
                ],
                "additionalProperties": false
            },
            "created_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "customer_hash": {
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
                                        "null",
                                        "number"
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
            },
            "email": {
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
            "has_uncommited_changes": {
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
            "last_name": {
                "type": [
                    "null",
                    "string"
                ]
            },
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
                                    ]
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
            },
            "note": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "note_attributes": {
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
            },
            "processed_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "processor_name": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "scheduled_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "shipments_count": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "shipping_address": {
                "properties": {
                    "address1": {
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
                    "last_name": {
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
                    "province": {
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
                ],
                "additionalProperties": false
            },
            "shipping_lines": {
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
            },
            "shopify_order_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "status": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "sub_total": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "subtotal_price": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "tags": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "tax_lines": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_discounts": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_line_items_price": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_price": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_refunds": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_tax": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_weight": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "transaction_id": {
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
            },
            "updated_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "charges",
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address_id"
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
                "browser_ip"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "client_details"
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
                "customer_hash"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "customer_id"
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
                "first_name"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "has_uncommited_changes"
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
                "last_name"
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
                "processed_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "processor_name"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "scheduled_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipments_count"
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
                "shopify_order_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "status"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "sub_total"
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
                "tags"
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
                "total_refunds"
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
                "transaction_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "type"
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
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""


recharge_collections = """{
    "type": "SCHEMA",
  "stream":  "collections",
            "key_properties": [
                "id"
            ],
            "schema": {
                "properties": {
                    "created_at": {
                        "format": "date-time",
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
                    "updated_at": {
                        "format": "date-time",
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                },
                "type": "object",
                "additionalProperties": false
            },
            "stream": "collections",
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
                        "inclusion": "available",
                        "selected": false
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "created_at"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": false
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
                        "selected": false
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "updated_at"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": false
                    }
                }
            ]
        }"""


recharge_customers = """{
            "type": "SCHEMA",
            "stream":"customers",
            "key_properties": [
                "id"
            ],
            "schema": {
                "properties": {
                    "id": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "hash": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "shopify_customer_id": {
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
                    "created_at": {
                        "format": "date-time",
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "updated_at": {
                        "format": "date-time",
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
                    "last_name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "billing_address1": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "billing_address2": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "billing_zip": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "billing_city": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "billing_company": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "billing_province": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "billing_country": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "billing_phone": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "processor_type": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "status": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "paypal_customer_token": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "braintree_customer_token": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "has_valid_payment_method": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "reason_payment_method_not_valid": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "has_card_error_in_dunning": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "number_active_subscriptions": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "number_subscriptions": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "first_charge_processed_at": {
                        "format": "date-time",
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                },
                "type": "object",
                "additionalProperties": false
            },
            "stream": "customers",
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
                        "hash"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "shopify_customer_id"
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
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "first_name"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "last_name"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "billing_address1"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "billing_address2"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "billing_zip"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "billing_city"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "billing_company"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "billing_province"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "billing_country"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "billing_phone"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "processor_type"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "status"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "paypal_customer_token"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "braintree_customer_token"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "has_valid_payment_method"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "reason_payment_method_not_valid"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "has_card_error_in_dunning"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "number_active_subscriptions"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "number_subscriptions"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "first_charge_processed_at"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                }
            ]
        }"""


recharge_discounts = """{
            "type": "SCHEMA",
             "stream":"discounts",
            "key_properties": [
                "id"
            ],
            "schema": {
                "properties": {
                    "id": {
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
                    "value": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },

                    "discount_type": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },

                    "ends_at": {
                        "format": "date-time",
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "starts_at": {
                        "format": "date-time",
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "status": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "usage_limit": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "applies_to_id": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "applies_to_resource": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "times_used": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "duration": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "duration_usage_limit": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "applies_to_product_type": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "created_at": {
                        "format": "date-time",
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "updated_at": {
                        "format": "date-time",
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "once_per_customer": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    }
                },
                "type": "object",
                "additionalProperties": false
            },
            "stream": "discounts",
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
                        "code"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "value"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "ends_at"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "starts_at"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "status"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "usage_limit"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "applies_to_id"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "applies_to_resource"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "times_used"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "duration"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "duration_usage_limit"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "applies_to_product_type"
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
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "once_per_customer"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                }
            ]
        }"""


recharge_metafields_store = """{
    "type": "SCHEMA",
    "stream": "metafields_store",
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "description": {
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
            "key": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "namespace": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "owner_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "owner_resource": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "updated_at": {
                "format": "date-time",
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
            },
            "value_type": {
                "type": [
                    "null",
                    "string"
                ]
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "metafields_store",
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
                "description"
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
                "key"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "namespace"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "owner_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "owner_resource"
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "value"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "value_type"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""


recharge_metafields_customer = """{
    "type": "SCHEMA",
    "stream": "metafields_customer",
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "description": {
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
            "key": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "namespace": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "owner_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "owner_resource": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "updated_at": {
                "format": "date-time",
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
            },
            "value_type": {
                "type": [
                    "null",
                    "string"
                ]
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "metafields_customer",
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
                "description"
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
                "key"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "namespace"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "owner_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "owner_resource"
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "value"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "value_type"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""


recharge_metafields_subscription = """{
    "type": "SCHEMA",
    "stream": "metafields_subscription",
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "description": {
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
            "key": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "namespace": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "owner_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "owner_resource": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "updated_at": {
                "format": "date-time",
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
            },
            "value_type": {
                "type": [
                    "null",
                    "string"
                ]
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "metafields_subscription",
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
                "description"
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
                "key"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "namespace"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "owner_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "owner_resource"
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "value"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "value_type"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""


recharge_onetimes = """{
    "type": "SCHEMA",
    "stream": "onetimes",
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "address_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "created_at": {
                "format": "date-time",
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
            "id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "next_charge_scheduled_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "price": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "product_title": {
                "type": [
                    "null",
                    "string"
                ]
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
            },
            "quantity": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "recharge_product_id": {
                "type": [
                    "null",
                    "string"
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
            "status": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "updated_at": {
                "format": "date-time",
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
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "onetimes",
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address_id"
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
                "customer_id"
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
                "next_charge_scheduled_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "price"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "product_title"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "properties"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "quantity"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "recharge_product_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_product_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_variant_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "sku"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "status"
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "variant_title"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""


recharge_orders = """{

    "type": "SCHEMA",
  "stream": "orders",

    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "address_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "address_is_active": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "billing_address": {
                "properties": {
                    "address1": {
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
                    "last_name": {
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
                    "province": {
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
                ],
                "additionalProperties": false
            },
            "charge_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "charge_status": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "created_at": {
                "format": "date-time",
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
                                        "null",
                                        "number"
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
            },
            "email": {
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
            "hash": {
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
            "is_prepaid": {
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
            },
            "note": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "note_attributes": {
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
            },
            "payment_processor": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "processed_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "scheduled_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "shipped_date": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "shipping_address": {
                "properties": {
                    "address1": {
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
                    "last_name": {
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
                    "province": {
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
                ],
                "additionalProperties": false
            },
            "shipping_date": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "shipping_lines": {
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
            },
            "shopify_cart_token": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shopify_customer_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shopify_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shopify_order_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shopify_order_number": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "status": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "subtotal_price": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "tags": {
                "type": [
                    "null",
                    "string"
                ]
            },
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
            },
            "total_discounts": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_line_items_price": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_price": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_refunds": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_tax": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_weight": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "transaction_id": {
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
            },
            "updated_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "orders",
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address_is_active"
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
                "charge_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "charge_status"
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
                "customer_id"
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
                "first_name"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "hash"
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
                "is_prepaid"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "last_name"
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
                "payment_processor"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "processed_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "scheduled_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipped_date"
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
                "shipping_date"
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
                "shopify_cart_token"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_customer_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_order_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_order_number"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "status"
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
                "tags"
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
                "total_refunds"
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
                "transaction_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "type"
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
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""


recharge_products = """{
    "type": "SCHEMA",
    "stream": "products",
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "collection_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "created_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "discount_amount": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "discount_type": {
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
            "images": {
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
                },
                "type": [
                    "null",
                    "object"
                ],
                "additionalProperties": false
            },
            "product_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shopify_product_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "subscription_defaults": {
                "properties": {
                    "charge_interval_frequency": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "cutoff_day_of_month": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "cutoff_day_of_week": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "expire_after_specific_number_of_charges": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "handle": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "number_charges_until_expiration": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "order_day_of_month": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "order_day_of_week": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "order_interval_frequency": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "order_interval_frequency_options": {
                        "anyOf": [
                            {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                }
                            },
                            {
                                "type": "null"
                            }
                        ]
                    },
                    "order_interval_unit": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "storefront_purchase_options": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                },
                "type": [
                    "null",
                    "object"
                ],
                "additionalProperties": false
            },
            "title": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "updated_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "products",
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
                "inclusion": "available",
                "selected": false
            }
        },
        {
            "breadcrumb": [
                "properties",
                "collection_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": false
            }
        },
        {
            "breadcrumb": [
                "properties",
                "created_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": false
            }
        },
        {
            "breadcrumb": [
                "properties",
                "discount_amount"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": false
            }
        },
        {
            "breadcrumb": [
                "properties",
                "discount_type"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": false
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
                "images"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": false
            }
        },
        {
            "breadcrumb": [
                "properties",
                "product_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": false
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_product_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": false
            }
        },
        {
            "breadcrumb": [
                "properties",
                "subscription_defaults"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": false
            }
        },
        {
            "breadcrumb": [
                "properties",
                "title"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": false
            }
        },
        {
            "breadcrumb": [
                "properties",
                "updated_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": false
            }
        }
    ]
}"""


recharge_shop = """{
    "type": "SCHEMA",
    "stream": "shop",
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "checkout_logo_url": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "created_at": {
                "format": "date-time",
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
            "domain": {
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
            "iana_timezone": {
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
            "my_shopify_domain": {
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
            "shop_email": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shop_phone": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "timezone": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "updated_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "shop",
    "metadata": [
        {
            "breadcrumb": [],
            "metadata": {
                "table-key-properties": [
                    "id"
                ],
                "forced-replication-method": "FULL_TABLE",
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "checkout_logo_url"
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
                "domain"
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
                "iana_timezone"
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
                "my_shopify_domain"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
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
                "shop_email"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shop_phone"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "timezone"
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
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""


recharge_subscriptions = """{
    "type": "SCHEMA",
    "stream": "subscriptions",
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "address_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "cancellation_reason": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "cancellation_reason_comments": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "cancelled_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "charge_interval_frequency": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "created_at": {
                "format": "date-time",
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
            "expire_after_specific_number_of_charges": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "has_queued_charges": {
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
            "is_skippable": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "is_swappable": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "max_retries_reached": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "next_charge_scheduled_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "order_day_of_month": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "order_day_of_week": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "order_interval_frequency": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "order_interval_unit": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "price": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "product_title": {
                "type": [
                    "null",
                    "string"
                ]
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
            },
            "quantity": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "recharge_product_id": {
                "type": [
                    "null",
                    "string"
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
            "sku_override": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "status": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "updated_at": {
                "format": "date-time",
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
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "subscriptions",
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "cancellation_reason"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "cancellation_reason_comments"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "cancelled_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "charge_interval_frequency"
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
                "customer_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "expire_after_specific_number_of_charges"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "has_queued_charges"
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
                "is_skippable"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "is_swappable"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "max_retries_reached"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "next_charge_scheduled_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "order_day_of_month"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "order_day_of_week"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "order_interval_frequency"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "order_interval_unit"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "price"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "product_title"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "properties"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "quantity"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "recharge_product_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_product_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_variant_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "sku"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "sku_override"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "status"
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
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "variant_title"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""