create table tests
(
    id            bigint,
    test_id       text,
    instrument    text,
    date          text,
    time          text,
    standard      text,
    concentration double precision,
    mass_mode     text,
    polarity      text,
    scan_type     text,
    scan_rate     bigint,
    n_scans       bigint
);

alter table tests
    owner to postgres;

create index ix_tests_id
    on tests (id);

