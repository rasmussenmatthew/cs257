'''
Nacho Rodriguez-Cortes
Matthew Rasmussen
2/19/2021
'''

CREATE TABLE public.weapons(
    id integer,
    name text,
    cost text,
    weight integer,
    weapon_category text,
    damage_die text,
    damage_type text,
    properties text,
    two_handed_dmg text
);

CREATE TABLE public.weapon_range(
    normal integer,
    long integer
);

CREATE TABLE public.armor(
    name text,
    cost text,
    weight integer,
    str_minimum integer,
    stealth_disadvantage boolean,
    base_armor_class integer,
    dex_bonus boolean,
    max_bonus integer,
    armor_catgegory text
);

CREATE TABLE public.tools(
    name text,
    cost text,
    weight integer,
    description text,
    tool_category text
);

CREATE TABLE public.adventuring_gear(
    name text,
    cost text,
    weight integer,
    description text,
    quantity integer
);

CREATE TABLE public.mounts(
    name text,
    cost text,
    weight integer,
    vehicle_category text,
    speed text,
    capacity integer
);

CREATE TABLE public.spells(
    id integer,
    spell_name text,
    spell_description text,
    higher_level text,
    components text,
    material text,
    ritual boolean,
    duration text,
    concentration boolean,
    casting_time text,
    spell_level integer,
    attack_type text,
    damage_information text,
    school text,
    classes text,
    dc_information text,
    heal_at_level text
);

CREATE TABLE public.spell_measurments (
    spell_id integer,
    spell_range text,
    area_of_effect_shape text,
    area_of_effect_range integer
);
