create table specifications
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

create index ix_specifications_id
    on specifications (id);

