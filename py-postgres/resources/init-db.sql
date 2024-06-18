--
-- SCHEMAS
--
CREATE SCHEMA IF NOT EXISTS development;

--
-- TABLES
--
create table development.user_score_history
(
    name       text,
    email      text,
    document   text     not null,
    score      integer  default 0,
    updated_at date     not null
);

alter table development.user_score_history owner to "app-user";
create index index_development_user_score_history_document
    on development.user_score_history(document);
