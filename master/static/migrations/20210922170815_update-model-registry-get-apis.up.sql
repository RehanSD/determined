CREATE TABLE public.modelsv2 (
	id integer NOT NULL,
	name character varying UNIQUE NOT NULL,
	description character varying,
	metadata jsonb,
	creation_time timestamp with time zone NOT NULL,
	last_updated_time timestamp with time zone,
    num_versions integer DEFAULT 0 NOT NULL,
    labels text[],
    readme text,
    username text,
    archived boolean DEFAULT false NOT NULL,

	CONSTRAINT models_pkey PRIMARY KEY (id)
);

ALTER TABLE public.modelsv2 ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.models_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);

CREATE TABLE public.model_versionsv2 (
	version integer NOT NULL,
	model integer NOT NULL,
	checkpoint_uuid uuid NOT NULL,
	creation_time timestamp with time zone NOT NULL,
	last_updated_time timestamp with time zone,
	metadata jsonb,

	CONSTRAINT model_and_version_unique UNIQUE (model, version),
	CONSTRAINT model_versions_pkey PRIMARY KEY (model, version),
	FOREIGN KEY(model) REFERENCES public.modelsv2(id),
	FOREIGN KEY(checkpoint_uuid) REFERENCES public.checkpoints(uuid)
);

INSERT INTO public.modelsv2 SELECT * FROM public.models;

WITH id_name_map as (
    SELECT mv.version, m.id, mv.checkpoint_uuid, mv.creation_time, mv.last_updated_time, mv.metadata 
    FROM public.modelsv2 as m
    JOIN public.model_versions as mv on mv.model_name = m.name
)
INSERT INTO public.model_versionsv2 SELECT * FROM id_name_map;

DROP TABLE public.models;

DROP TABLE public.model_versions;
