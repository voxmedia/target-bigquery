klaviyo_bounce = """{"type": "SCHEMA", 
      "stream": "bounce",
      "tap_stream_id": "KU6iPf",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string"
          },
          "event_name": {
            "type": "string"
          },
          "timestamp": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "datetime": {
            "type": "string",
            "format": "date-time"
          },
          "statistic_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "event_properties": {
            "type": "object",
            "properties":{
              "campaign_name":{"type": "string"},
              "message":{"type": "string"},
              "_cohortmessage_send_cohort":{"type": "string"},
              "flow":{"type": "string"},
              "subject":{"type": "string"},
              "email_domain":{"type": "string"},
              "bounce_type":{"type": "string"},
              "event_id":{"type": "string"}
            }
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "INCREMENTAL",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "uuid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "datetime"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "statistic_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_properties"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_click = """{
      "type": "SCHEMA", 
      "stream": "click",
      "tap_stream_id": "Kh5gcC",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string"
          },
          "event_name": {
            "type": "string"
          },
          "timestamp": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "datetime": {
            "type": "string",
            "format": "date-time"
          },
          "statistic_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "event_properties": {
            "type": "object",
            "properties": {
              "campaign_name":{"type": "string"},
              "event_id":{"type": "string"},
              "email_domain":{"type": "string"},
              "_cohortmessage_send_cohort":{"type": "string"},
              "url":{"type": "string"},
              "message_interaction":{"type": "string"},
              "client_type":{"type": "string"},
              "flow":{"type": "string"},
              "client_os_family":{"type": "string"},
              "message":{"type": "string"},
              "subject":{"type": "string"},
              "client_name":{"type": "string"},
              "client_os":{"type": "string"}
            }
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "INCREMENTAL",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "uuid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "datetime"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "statistic_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_properties"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_email = """{
      "type": "SCHEMA", 
      "stream": "dropped_email",
      "tap_stream_id": "J7EriL",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string"
          },
          "event_name": {
            "type": "string"
          },
          "timestamp": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "datetime": {
            "type": "string",
            "format": "date-time"
          },
          "statistic_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "event_properties": {
            "type": "object",
            "properties": {
              "campaign_name":{"type": "string"},
              "message":{"type": "string"},
              "_cohortmessage_send_cohort":{"type": "string"},
              "flow":{"type": "string"},
              "subject":{"type": "string"},
              "email_domain":{"type": "string"},
              "email_id":{"type": "string"}
            }
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "INCREMENTAL",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "uuid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "datetime"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "statistic_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_properties"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_mark_as_spam = """{
      "type": "SCHEMA", 
      "stream": "mark_as_spam",
      "tap_stream_id": "PuW5Qd",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string"
          },
          "event_name": {
            "type": "string"
          },
          "timestamp": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "datetime": {
            "type": "string",
            "format": "date-time"
          },
          "statistic_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "event_properties": {
            "type": "object",
            "properties": {
              "campaign_name":{"type": "string"},
              "message":{"type": "string"},
              "_cohortmessage_send_cohort":{"type": "string"},
              "flow":{"type": "string"},
              "subject":{"type": "string"},
              "email_domain":{"type": "string"},
              "email_id":{"type": "string"}
            }
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "INCREMENTAL",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "uuid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "datetime"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "statistic_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_properties"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_open = """{
      "type": "SCHEMA", 
      "stream": "open",
      "tap_stream_id": "HuDnG9",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string"
          },
          "event_name": {
            "type": "string"
          },
          "timestamp": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "datetime": {
            "type": "string",
            "format": "date-time"
          },
          "statistic_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "event_properties": {
            "type": "object",
            "properties": {
              "campaign_name":{"type": "string"},
              "event_id":{"type": "string"},
              "email_domain":{"type": "string"},
              "client_canonical":{"type": "string"},
              "_cohortmessage_send_cohort":{"type": "string"},
              "url":{"type": "string"},
              "message_interaction":{"type": "string"},
              "client_type":{"type": "string"},
              "flow":{"type": "string"},
              "client_os_family":{"type": "string"},
              "message":{"type": "string"},
              "subject":{"type": "string"},
              "client_name":{"type": "string"},
              "client_os":{"type": "string"}
            }
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "INCREMENTAL",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "uuid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "datetime"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "statistic_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_properties"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_receive = """{
      "type": "SCHEMA", 
      "stream": "receive",
      "tap_stream_id": "M5v9H7",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string"
          },
          "event_name": {
            "type": "string"
          },
          "timestamp": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "datetime": {
            "type": "string",
            "format": "date-time"
          },
          "statistic_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "event_properties": {
            "type": "object",
            "properties": {
              "campaign_name":{"type": "string"},
              "message":{"type": "string"},
              "_cohortmessage_send_cohort":{"type": "string"},
              "flow":{"type": "string"},
              "subject":{"type": "string"},
              "email_domain":{"type": "string"},
              "event_id":{"type": "string"}
            }
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "INCREMENTAL",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "uuid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "datetime"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "statistic_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_properties"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_subscribe_list = """{
      "type": "SCHEMA", 
      "stream": "subscribe_list",
      "tap_stream_id": "JPRxJ3",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string"
          },
          "event_name": {
            "type": "string"
          },
          "timestamp": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "datetime": {
            "type": "string",
            "format": "date-time"
          },
          "statistic_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "event_properties": {
            "type": "object",
            "properties": {
              "list": {
                "type": "string"
              },
              "event_id": {
                "type": "string"
              }
            }
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "INCREMENTAL",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "uuid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "datetime"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "statistic_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_properties"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_unsubscribe = """{
      "type": "SCHEMA", 
      "stream": "unsubscribe",
      "tap_stream_id": "MGwcjJ",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string"
          },
          "event_name": {
            "type": "string"
          },
          "timestamp": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "datetime": {
            "type": "string",
            "format": "date-time"
          },
          "statistic_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "event_properties": {
            "type": "object",
            "properties": {
              "_cohortmessage_send_cohort":{"type": "string"},
              "campaign_name":{"type": "string"},
              "message":{"type": "string"},
              "email_domain":{"type": "string"},
              "event_id":{"type": "string"},
              "flow":{"type": "string"},
              "subject":{"type": "string"}
            }
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "INCREMENTAL",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "uuid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "datetime"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "statistic_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_properties"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_unsub_list = """{
      "type": "SCHEMA", 
      "stream": "unsub_list",
      "tap_stream_id": "Hq4hfW",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string"
          },
          "event_name": {
            "type": "string"
          },
          "timestamp": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "datetime": {
            "type": "string",
            "format": "date-time"
          },
          "statistic_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "event_properties": {
            "type": "object",
            "properties": {
              "list": {
                "type": "string"
              },
              "event_id": {
                "type": "string"
              }
            }
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "INCREMENTAL",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "uuid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "datetime"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "statistic_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_properties"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_update_email_preferences = """{
      "type": "SCHEMA", 
      "stream": "update_email_preferences",
      "tap_stream_id": "HVE24G",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string"
          },
          "event_name": {
            "type": "string"
          },
          "timestamp": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "datetime": {
            "type": "string",
            "format": "date-time"
          },
          "statistic_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "event_properties": {
            "type": "object",
            "properties": {
              "list": {
                "type": "string"
              },
              "event_id": {
                "type": "string"
              }
            }
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            }
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "INCREMENTAL",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "uuid"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "datetime"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "statistic_id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "event_properties"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_global_exclusions = """{
      "type": "SCHEMA", 
      "stream": "global_exclusions",
      "tap_stream_id": "global_exclusions",
      "key_properties": [
        "email"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "timestamp": {
            "type": "string",
            "format": "date-time"
          },
          "reason": {
            "type": "string"
          },
          "object": {
            "type": "string"
          },
          "email": {
            "type": "string"
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "email",
            "forced-replication-method": "FULL_TABLE",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "timestamp"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "reason"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "email"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""
klaviyo_lists = """{
      "type": "SCHEMA", 
      "stream": "lists",
      "tap_stream_id": "lists",
      "key_properties": [
        "id"
      ],
      "schema": {
        "type": "object",
        "properties": {
          "created": {
            "type": "string",
            "format": "date-time"
          },
          "updated": {
            "type": "string",
            "format": "date-time"
          },
          "person_count": {
            "type": "integer"
          },
          "object": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "id": {
            "type": "string"
          }
        }
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": "id",
            "forced-replication-method": "FULL_TABLE",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "updated"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "person_count"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "object"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "type"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "id"
          ],
          "metadata": {
            "inclusion": "automatic",
            "selected": true
          }
        }
      ]
    }"""