create table results
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

create index ix_results_id
    on results (id);

