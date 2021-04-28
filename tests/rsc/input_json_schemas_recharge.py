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

