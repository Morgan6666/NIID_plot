create table standards
(
    id          bigint,
    standard    text,
    polarity    text,
    target_mass double precision
);

alter table standards
    owner to postgres;

create index ix_standards_id
    on standards (id);

