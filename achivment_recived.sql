--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.4

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
-- Name: achivment_recived; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.achivment_recived (
    achivment_recived_id integer NOT NULL,
    user_id integer NOT NULL,
    achivment_id integer NOT NULL,
    date_of_recived timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.achivment_recived OWNER TO postgres;

--
-- Name: achivment_recived_achivment_recived_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.achivment_recived_achivment_recived_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.achivment_recived_achivment_recived_id_seq OWNER TO postgres;

--
-- Name: achivment_recived_achivment_recived_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.achivment_recived_achivment_recived_id_seq OWNED BY public.achivment_recived.achivment_recived_id;


--
-- Name: achivments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.achivments (
    achivment_id integer NOT NULL,
    achivment_name character varying(140) NOT NULL,
    number_of_points integer
);


ALTER TABLE public.achivments OWNER TO postgres;

--
-- Name: achivments_achivment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.achivments_achivment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.achivments_achivment_id_seq OWNER TO postgres;

--
-- Name: achivments_achivment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.achivments_achivment_id_seq OWNED BY public.achivments.achivment_id;


--
-- Name: description; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.description (
    description_id integer NOT NULL,
    language_name character varying(40) NOT NULL,
    achivment_id integer NOT NULL,
    description text
);


ALTER TABLE public.description OWNER TO postgres;

--
-- Name: description_description_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.description_description_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.description_description_id_seq OWNER TO postgres;

--
-- Name: description_description_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.description_description_id_seq OWNED BY public.description.description_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    name_user character varying(40) NOT NULL,
    language_name character varying(40) NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: achivment_recived achivment_recived_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.achivment_recived ALTER COLUMN achivment_recived_id SET DEFAULT nextval('public.achivment_recived_achivment_recived_id_seq'::regclass);


--
-- Name: achivments achivment_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.achivments ALTER COLUMN achivment_id SET DEFAULT nextval('public.achivments_achivment_id_seq'::regclass);


--
-- Name: description description_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.description ALTER COLUMN description_id SET DEFAULT nextval('public.description_description_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: achivment_recived; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.achivment_recived (achivment_recived_id, user_id, achivment_id, date_of_recived) FROM stdin;
3	2	2	2024-10-06 12:27:25.893784
4	1	1	2024-10-08 00:50:11.751137
6	1	1	2024-10-08 01:11:03.610124
24	1	1	2024-10-08 09:56:01.493125
1	1	4	2024-10-06 12:24:54.921514
27	3	4	2024-10-08 21:13:20.540215
28	3	4	2024-10-08 21:13:20.540215
29	3	4	2024-10-08 21:13:20.540215
30	1	1	2024-09-21 12:24:54.921514
31	1	1	2024-09-30 12:24:54.921514
32	1	1	2024-10-01 12:24:54.921514
33	1	1	2024-10-02 12:24:54.921514
34	1	1	2024-10-03 12:24:54.921514
35	1	1	2024-10-04 12:24:54.921514
36	1	1	2024-10-05 12:24:54.921514
38	1	1	2024-10-07 12:24:54.921514
39	1	1	2024-10-06 12:24:54.921514
40	1	3	2024-10-09 13:37:07.646999
41	4	14	2024-10-09 13:37:13.573053
42	5	14	2024-10-09 13:37:16.28302
43	7	14	2024-10-09 13:37:18.396275
44	8	13	2024-10-09 13:37:23.279041
\.


--
-- Data for Name: achivments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.achivments (achivment_id, achivment_name, number_of_points) FROM stdin;
1	Отразите попадание щитом.	100
2	Получите обсидиан	1000
3	Добудьте алмазы	100
4	Постройте, зажгите и войдите в портал Незера	100
5	Алмазная броня спасает жизни	2000
8	Обновите свою кирку	234
9	Наберите ведро лавы	5432
10	Защитите себя железной бронёй	23423
11	Выплавьте железный слиток	123
12	Сделайте кирку попрочней	6000
13	Добудьте камень новой киркой	200
14	Главная история игры	100
\.


--
-- Data for Name: description; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.description (description_id, language_name, achivment_id, description) FROM stdin;
1	ru	14	Необходимо иметь любую часть алмазной брони в инвентаре.
2	en	14	You must have any piece of diamond armor in your inventory.
5	en	13	Enter the Nether dimension.
6	ru	13	Войдите в измерение Незер.
7	en	12	You must have a diamond in your inventory.
8	ru	12	Необходимо иметь алмаз в инвентаре.
9	en	11	You must have obsidian in your inventory.
10	ru	11	Необходимо иметь обсидиан в инвентаре.
11	en	10	Reflect any projectile with your shield.
12	ru	10	Отразите щитом любой снаряд.
13	en	9	You must have an iron pickaxe in your inventory.
14	ru	9	Необходимо иметь железную кирку в инвентаре.
15	en	8	You must have a bucket of lava in your inventory.
16	ru	8	Необходимо иметь ведро лавы в инвентаре.
17	en	5	You must have any piece of iron armor in your inventory.
18	ru	5	Необходимо иметь любую часть железной брони в инвентаре.
19	en	4	You must have an iron ingot in your inventory.
20	ru	4	Необходимо иметь железный слиток в инвентаре.
21	en	3	You must have a stone pickaxe in your inventory.
22	ru	3	Необходимо иметь каменную кирку в инвентаре.
23	en	2	You must have one of the following three stone blocks from the tag in your inventory
24	ru	2	Необходимо иметь в инвентаре один из следующих трёх каменных блоков из тега
25	en	1	Get a workbench.
26	ru	1	Получите верстак.
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, name_user, language_name) FROM stdin;
1	MC BOB	en
2	Chedona	ru
3	aboba	en
4	Jmihenko Valieriy	en
5	Jmarius	ru
6	cyborg	en
7	Goroh	ru
8	Patarius	en
9	arsenchik	ru
10	jorik	en
\.


--
-- Name: achivment_recived_achivment_recived_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.achivment_recived_achivment_recived_id_seq', 44, true);


--
-- Name: achivments_achivment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.achivments_achivment_id_seq', 14, true);


--
-- Name: description_description_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.description_description_id_seq', 26, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 10, true);


--
-- Name: achivment_recived achivment_recived_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.achivment_recived
    ADD CONSTRAINT achivment_recived_pkey PRIMARY KEY (achivment_recived_id);


--
-- Name: achivments achivments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.achivments
    ADD CONSTRAINT achivments_pkey PRIMARY KEY (achivment_id);


--
-- Name: description description_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.description
    ADD CONSTRAINT description_pkey PRIMARY KEY (description_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: achivment_recived fk_achivment_recived_achivments_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.achivment_recived
    ADD CONSTRAINT fk_achivment_recived_achivments_id FOREIGN KEY (achivment_id) REFERENCES public.achivments(achivment_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: achivment_recived fk_aichivment_recived_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.achivment_recived
    ADD CONSTRAINT fk_aichivment_recived_users_id FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: description fk_description_achivment_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.description
    ADD CONSTRAINT fk_description_achivment_id FOREIGN KEY (achivment_id) REFERENCES public.achivments(achivment_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

