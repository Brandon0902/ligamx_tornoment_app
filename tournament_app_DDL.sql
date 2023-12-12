--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: director_tecnico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.director_tecnico (
    id integer NOT NULL,
    nombre character varying(30) NOT NULL,
    nacionalidad character varying(20) NOT NULL,
    porcentaje double precision NOT NULL
);


ALTER TABLE public.director_tecnico OWNER TO postgres;

--
-- Name: director_tecnico_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.director_tecnico_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.director_tecnico_id_seq OWNER TO postgres;

--
-- Name: director_tecnico_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.director_tecnico_id_seq OWNED BY public.director_tecnico.id;


--
-- Name: equipo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipo (
    id integer NOT NULL,
    logotipo bytea NOT NULL,
    nombre character varying(30) NOT NULL,
    director_tecnico_id integer
);


ALTER TABLE public.equipo OWNER TO postgres;

--
-- Name: equipo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.equipo_id_seq OWNER TO postgres;

--
-- Name: equipo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipo_id_seq OWNED BY public.equipo.id;


--
-- Name: equipo_torneo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipo_torneo (
    id integer NOT NULL,
    torneo_id integer,
    equipo_id integer,
    goles integer NOT NULL,
    puntos integer NOT NULL,
    partidos_ganados integer NOT NULL,
    partidos_empatados integer NOT NULL,
    partidos_perdidos integer NOT NULL
);


ALTER TABLE public.equipo_torneo OWNER TO postgres;

--
-- Name: equipo_torneo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipo_torneo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.equipo_torneo_id_seq OWNER TO postgres;

--
-- Name: equipo_torneo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipo_torneo_id_seq OWNED BY public.equipo_torneo.id;


--
-- Name: jugador; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jugador (
    id integer NOT NULL,
    equipo_id integer,
    nombre character varying(30) NOT NULL,
    numero integer NOT NULL,
    nacionalidad character varying(20) NOT NULL,
    posicion character varying(20) NOT NULL,
    rol character varying(20) NOT NULL
);


ALTER TABLE public.jugador OWNER TO postgres;

--
-- Name: jugador_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jugador_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.jugador_id_seq OWNER TO postgres;

--
-- Name: jugador_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jugador_id_seq OWNED BY public.jugador.id;


--
-- Name: partido; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.partido (
    id integer NOT NULL,
    torneo_id integer,
    equipo1_id integer,
    equipo2_id integer,
    estadio character varying(20) NOT NULL,
    fecha timestamp without time zone NOT NULL
);


ALTER TABLE public.partido OWNER TO postgres;

--
-- Name: partido_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.partido_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.partido_id_seq OWNER TO postgres;

--
-- Name: partido_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.partido_id_seq OWNED BY public.partido.id;


--
-- Name: partido_resultado; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.partido_resultado (
    id integer NOT NULL,
    torneo integer,
    equipo1 integer,
    equipo2 integer,
    estadio character varying(20) NOT NULL,
    fecha timestamp without time zone NOT NULL,
    resultado integer
);


ALTER TABLE public.partido_resultado OWNER TO postgres;

--
-- Name: partido_resultado_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.partido_resultado_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.partido_resultado_id_seq OWNER TO postgres;

--
-- Name: partido_resultado_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.partido_resultado_id_seq OWNED BY public.partido_resultado.id;


--
-- Name: resultado; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resultado (
    id integer NOT NULL,
    partido_id integer,
    goles_equipo1 integer NOT NULL,
    goles_equipo2 integer NOT NULL
);


ALTER TABLE public.resultado OWNER TO postgres;

--
-- Name: resultado_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resultado_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.resultado_id_seq OWNER TO postgres;

--
-- Name: resultado_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resultado_id_seq OWNED BY public.resultado.id;


--
-- Name: tabla_posiciones_equipo_torneo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tabla_posiciones_equipo_torneo (
    id integer NOT NULL,
    tabla_posiciones_id integer,
    equipo_torneo_id integer
);


ALTER TABLE public.tabla_posiciones_equipo_torneo OWNER TO postgres;

--
-- Name: tabla_posiciones_equipo_torneo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tabla_posiciones_equipo_torneo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tabla_posiciones_equipo_torneo_id_seq OWNER TO postgres;

--
-- Name: tabla_posiciones_equipo_torneo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tabla_posiciones_equipo_torneo_id_seq OWNED BY public.tabla_posiciones_equipo_torneo.id;


--
-- Name: tablaposiciones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tablaposiciones (
    id integer NOT NULL,
    torneo_id integer
);


ALTER TABLE public.tablaposiciones OWNER TO postgres;

--
-- Name: tablaposiciones_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tablaposiciones_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tablaposiciones_id_seq OWNER TO postgres;

--
-- Name: tablaposiciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tablaposiciones_id_seq OWNED BY public.tablaposiciones.id;


--
-- Name: torneo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.torneo (
    id integer NOT NULL,
    fecha character varying(15) NOT NULL,
    nombre character varying(30) NOT NULL
);


ALTER TABLE public.torneo OWNER TO postgres;

--
-- Name: torneo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.torneo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.torneo_id_seq OWNER TO postgres;

--
-- Name: torneo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.torneo_id_seq OWNED BY public.torneo.id;


--
-- Name: director_tecnico id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director_tecnico ALTER COLUMN id SET DEFAULT nextval('public.director_tecnico_id_seq'::regclass);


--
-- Name: equipo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo ALTER COLUMN id SET DEFAULT nextval('public.equipo_id_seq'::regclass);


--
-- Name: equipo_torneo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_torneo ALTER COLUMN id SET DEFAULT nextval('public.equipo_torneo_id_seq'::regclass);


--
-- Name: jugador id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jugador ALTER COLUMN id SET DEFAULT nextval('public.jugador_id_seq'::regclass);


--
-- Name: partido id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partido ALTER COLUMN id SET DEFAULT nextval('public.partido_id_seq'::regclass);


--
-- Name: partido_resultado id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partido_resultado ALTER COLUMN id SET DEFAULT nextval('public.partido_resultado_id_seq'::regclass);


--
-- Name: resultado id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resultado ALTER COLUMN id SET DEFAULT nextval('public.resultado_id_seq'::regclass);


--
-- Name: tabla_posiciones_equipo_torneo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tabla_posiciones_equipo_torneo ALTER COLUMN id SET DEFAULT nextval('public.tabla_posiciones_equipo_torneo_id_seq'::regclass);


--
-- Name: tablaposiciones id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tablaposiciones ALTER COLUMN id SET DEFAULT nextval('public.tablaposiciones_id_seq'::regclass);


--
-- Name: torneo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.torneo ALTER COLUMN id SET DEFAULT nextval('public.torneo_id_seq'::regclass);


--
-- Data for Name: director_tecnico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.director_tecnico (id, nombre, nacionalidad, porcentaje) FROM stdin;
\.


--
-- Data for Name: equipo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.equipo (id, logotipo, nombre, director_tecnico_id) FROM stdin;
\.


--
-- Data for Name: equipo_torneo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.equipo_torneo (id, torneo_id, equipo_id, goles, puntos, partidos_ganados, partidos_empatados, partidos_perdidos) FROM stdin;
\.


--
-- Data for Name: jugador; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jugador (id, equipo_id, nombre, numero, nacionalidad, posicion, rol) FROM stdin;
\.


--
-- Data for Name: partido; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.partido (id, torneo_id, equipo1_id, equipo2_id, estadio, fecha) FROM stdin;
\.


--
-- Data for Name: partido_resultado; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.partido_resultado (id, torneo, equipo1, equipo2, estadio, fecha, resultado) FROM stdin;
\.


--
-- Data for Name: resultado; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.resultado (id, partido_id, goles_equipo1, goles_equipo2) FROM stdin;
\.


--
-- Data for Name: tabla_posiciones_equipo_torneo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tabla_posiciones_equipo_torneo (id, tabla_posiciones_id, equipo_torneo_id) FROM stdin;
\.


--
-- Data for Name: tablaposiciones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tablaposiciones (id, torneo_id) FROM stdin;
\.


--
-- Data for Name: torneo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.torneo (id, fecha, nombre) FROM stdin;
\.


--
-- Name: director_tecnico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.director_tecnico_id_seq', 1, false);


--
-- Name: equipo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.equipo_id_seq', 1, false);


--
-- Name: equipo_torneo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.equipo_torneo_id_seq', 1, false);


--
-- Name: jugador_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jugador_id_seq', 1, false);


--
-- Name: partido_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.partido_id_seq', 1, false);


--
-- Name: partido_resultado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.partido_resultado_id_seq', 1, false);


--
-- Name: resultado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resultado_id_seq', 1, false);


--
-- Name: tabla_posiciones_equipo_torneo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tabla_posiciones_equipo_torneo_id_seq', 1, false);


--
-- Name: tablaposiciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tablaposiciones_id_seq', 1, false);


--
-- Name: torneo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.torneo_id_seq', 1, false);


--
-- Name: director_tecnico director_tecnico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director_tecnico
    ADD CONSTRAINT director_tecnico_pkey PRIMARY KEY (id);


--
-- Name: equipo equipo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo
    ADD CONSTRAINT equipo_pkey PRIMARY KEY (id);


--
-- Name: equipo_torneo equipo_torneo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_torneo
    ADD CONSTRAINT equipo_torneo_pkey PRIMARY KEY (id);


--
-- Name: jugador jugador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jugador
    ADD CONSTRAINT jugador_pkey PRIMARY KEY (id);


--
-- Name: partido partido_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partido
    ADD CONSTRAINT partido_pkey PRIMARY KEY (id);


--
-- Name: partido_resultado partido_resultado_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partido_resultado
    ADD CONSTRAINT partido_resultado_pkey PRIMARY KEY (id);


--
-- Name: resultado resultado_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resultado
    ADD CONSTRAINT resultado_pkey PRIMARY KEY (id);


--
-- Name: tabla_posiciones_equipo_torneo tabla_posiciones_equipo_torneo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tabla_posiciones_equipo_torneo
    ADD CONSTRAINT tabla_posiciones_equipo_torneo_pkey PRIMARY KEY (id);


--
-- Name: tablaposiciones tablaposiciones_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tablaposiciones
    ADD CONSTRAINT tablaposiciones_pkey PRIMARY KEY (id);


--
-- Name: torneo torneo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.torneo
    ADD CONSTRAINT torneo_pkey PRIMARY KEY (id);


--
-- Name: equipo equipo_director_tecnico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo
    ADD CONSTRAINT equipo_director_tecnico_id_fkey FOREIGN KEY (director_tecnico_id) REFERENCES public.director_tecnico(id);


--
-- Name: equipo_torneo equipo_torneo_equipo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_torneo
    ADD CONSTRAINT equipo_torneo_equipo_id_fkey FOREIGN KEY (equipo_id) REFERENCES public.equipo(id);


--
-- Name: equipo_torneo equipo_torneo_torneo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_torneo
    ADD CONSTRAINT equipo_torneo_torneo_id_fkey FOREIGN KEY (torneo_id) REFERENCES public.torneo(id);


--
-- Name: jugador jugador_equipo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jugador
    ADD CONSTRAINT jugador_equipo_id_fkey FOREIGN KEY (equipo_id) REFERENCES public.equipo(id);


--
-- Name: partido partido_equipo1_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partido
    ADD CONSTRAINT partido_equipo1_id_fkey FOREIGN KEY (equipo1_id) REFERENCES public.equipo(id);


--
-- Name: partido partido_equipo2_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partido
    ADD CONSTRAINT partido_equipo2_id_fkey FOREIGN KEY (equipo2_id) REFERENCES public.equipo(id);


--
-- Name: partido_resultado partido_resultado_equipo1_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partido_resultado
    ADD CONSTRAINT partido_resultado_equipo1_fkey FOREIGN KEY (equipo1) REFERENCES public.equipo(id);


--
-- Name: partido_resultado partido_resultado_equipo2_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partido_resultado
    ADD CONSTRAINT partido_resultado_equipo2_fkey FOREIGN KEY (equipo2) REFERENCES public.equipo(id);


--
-- Name: partido_resultado partido_resultado_torneo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partido_resultado
    ADD CONSTRAINT partido_resultado_torneo_fkey FOREIGN KEY (torneo) REFERENCES public.torneo(id);


--
-- Name: partido partido_torneo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.partido
    ADD CONSTRAINT partido_torneo_id_fkey FOREIGN KEY (torneo_id) REFERENCES public.torneo(id);


--
-- Name: resultado resultado_partido_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resultado
    ADD CONSTRAINT resultado_partido_id_fkey FOREIGN KEY (partido_id) REFERENCES public.partido(id);


--
-- Name: tabla_posiciones_equipo_torneo tabla_posiciones_equipo_torneo_equipo_torneo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tabla_posiciones_equipo_torneo
    ADD CONSTRAINT tabla_posiciones_equipo_torneo_equipo_torneo_id_fkey FOREIGN KEY (equipo_torneo_id) REFERENCES public.equipo_torneo(id);


--
-- Name: tabla_posiciones_equipo_torneo tabla_posiciones_equipo_torneo_tabla_posiciones_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tabla_posiciones_equipo_torneo
    ADD CONSTRAINT tabla_posiciones_equipo_torneo_tabla_posiciones_id_fkey FOREIGN KEY (tabla_posiciones_id) REFERENCES public.tablaposiciones(id);


--
-- Name: tablaposiciones tablaposiciones_torneo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tablaposiciones
    ADD CONSTRAINT tablaposiciones_torneo_id_fkey FOREIGN KEY (torneo_id) REFERENCES public.torneo(id);


--
-- PostgreSQL database dump complete
--

