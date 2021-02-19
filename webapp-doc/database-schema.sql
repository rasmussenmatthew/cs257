'''
Nacho Rodriguez-Cortes
Matthew Rasmussen
2/19/2021
'''

CREATE TABLE public.races(
    id integer,
    name text,
    speed integer,
    alignment text,
    age text,
    size text,
    size_desc text,
    starting_proficiencies text,
    languages text,
    language_desc text,
    traits text,
    subraces text
);

CREATE TABLE public.ability_bonuses(
    race_id integer,
    str integer,
    dex integer,
    inte integer,
    wis integer,
    con integer,
    chr integer
);

CREATE TABLE public.classes(
    name text,
    hit_die integer,
    proficiency_choices text,
    proficiencies text,
    saving_throws text,
    subclasses text
);

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
    name text,
    description text,
    higher_level text,
    range text,
    components text,
    material text,
    ritual boolean,
    duration text,
    concentration boolean,
    casting_time text,
    level integer,
    attack_type text,
    damage_type text,
    damage_modifier text,
    school text,
    classes text,
    dc_type text,
    dc_success text,
    heal_at_level text,
    area_of_effect_shape text,
    area_of_effect_range integer
);

CREATE TABLE public.monsters(
    id integer,
    name text,
    size text,
    type text,
    subtype text,
    alignment text,
    armor_class integer,
    hit_point integer,
    hit_dice text,
    speed text,
    proficiencies text,
    vulnerabilities text,
    resistences text,
    dmg_immunities text,
    condition_immunities text,
    senses text,
    languages text,
    challenge_rating integer,
    special_abilities text,
    actions text,
    legendary_actions text,
    reactions text
);

CREATE TABLE public.monster_stats(
    monster_id integer,
    str integer,
    dex integer,
    inte integer,
    wis integer,
    con integer,
    chr integer
);
