-- ==========================================================
-- CyberSight AI Database Schema
-- ==========================================================
-- Description:
-- Creates the network_logs table used for storing
-- transformed UNSW-NB15 network traffic data.
-- ==========================================================

DROP TABLE IF EXISTS network_logs;

CREATE TABLE network_logs (

    -- ======================================================
    -- Primary Key
    -- ======================================================
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- ======================================================
    -- Original Dataset Columns
    -- ======================================================
    id INTEGER,

    dur REAL,

    proto TEXT,
    service TEXT,
    state TEXT,

    spkts INTEGER,
    dpkts INTEGER,

    sbytes INTEGER,
    dbytes INTEGER,

    rate REAL,

    sttl INTEGER,
    dttl INTEGER,

    sload REAL,
    dload REAL,

    sloss INTEGER,
    dloss INTEGER,

    sinpkt REAL,
    dinpkt REAL,

    sjit REAL,
    djit REAL,

    swin INTEGER,
    stcpb INTEGER,
    dtcpb INTEGER,
    dwin INTEGER,

    tcprtt REAL,
    synack REAL,
    ackdat REAL,

    smean INTEGER,
    dmean INTEGER,

    trans_depth INTEGER,
    response_body_len INTEGER,

    ct_srv_src INTEGER,
    ct_state_ttl INTEGER,
    ct_dst_ltm INTEGER,
    ct_src_dport_ltm INTEGER,
    ct_dst_sport_ltm INTEGER,
    ct_dst_src_ltm INTEGER,

    is_ftp_login INTEGER,
    ct_ftp_cmd INTEGER,
    ct_flw_http_mthd INTEGER,

    ct_src_ltm INTEGER,
    ct_srv_dst INTEGER,

    is_sm_ips_ports INTEGER,

    attack_cat TEXT,
    label INTEGER,

    dataset TEXT,

    -- ======================================================
    -- Engineered Features
    -- ======================================================
    total_bytes REAL,
    total_packets REAL,
    bytes_per_packet REAL,
    traffic_direction_ratio REAL,
    packet_direction_ratio REAL
);