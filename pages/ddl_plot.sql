create table if not exists tests
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

create index if not exists ix_tests_id
    on tests (id);

create table if not exists standards
(
    id          bigint,
    standard    text,
    polarity    text,
    target_mass double precision
);

alter table standards
    owner to postgres;

create index if not exists ix_standards_id
    on standards (id);

create table if not exists results
(
    id           bigint,
    test_id      text,
    target_mass  double precision,
    visible_mass double precision,
    intensity    double precision,
    width        double precision,
    mass_shift   double precision
);

alter table results
    owner to postgres;

create index if not exists ix_results_id
    on results (id);

create table if not exists specifications
(
    id                 bigint,
    standard           text,
    concentration      double precision,
    mass_mode          text,
    polarity           text,
    scan_type          text,
    scan_rate          bigint,
    n_scans            bigint,
    target_mass        double precision,
    min_intensity      double precision,
    min_width          double precision,
    max_width          double precision,
    max_abs_mass_shift double precision
);

alter table specifications
    owner to postgres;

create index if not exists ix_specifications_id
    on specifications (id);

