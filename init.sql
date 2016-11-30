CREATE DATABASE schedule;

CREATE TABLE schedule.teams (
    "id" integer DEFAULT nextval('teams_id_seq'::regclass),
    "name" text NOT NULL,
    PRIMARY KEY ("id"),
    UNIQUE ("name")
);

CREATE TABLE schedule.events (
    "id" integer DEFAULT nextval('events_id_seq'::regclass),
    "team1" integer NOT NULL,
    "team2" integer NOT NULL,
    "datetime" timestamp without time zone NOT NULL,
    "type" text NOT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT "events_team1_fkey" FOREIGN KEY ("team1") REFERENCES "".""(),
    CONSTRAINT "events_team2_fkey" FOREIGN KEY ("team2") REFERENCES "".""()
);
