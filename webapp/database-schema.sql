'''
Nacho Rodriguez-Cortes
Matthew Rasmussen
2/19/2021
'''

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
    area_of_effect_range text
);
