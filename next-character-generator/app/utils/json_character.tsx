export interface Character {
    name:          string;
    sex:           boolean;
    stats:         Stats;
    race:          Race;
    class:         Class;
    personality:   Personality;
    background:    Background;
    ideal:         Ideal;
    weakness:      Peculiarities;
    peculiarities: Peculiarities;
}

export interface Background {
    title: string;
    link:  string;
}

export interface Class {
    name: string;
    link: string;
}

export interface Ideal {
    description: string;
    worldview:   number;
}

export interface Peculiarities {
    description: string;
}

export interface Personality {
    first_letter:  string;
    second_letter: string;
    third_letter:  string;
    fourth_letter: string;
}

export interface Race {
    name:        string;
    description: string;
    link:        string;
    speed:       number;
}

export interface Stats {
    force:        number;
    charisma:     number;
    dexterity:    number;
    endurance:    number;
    intelligence: number;
    wisdom:       number;
}