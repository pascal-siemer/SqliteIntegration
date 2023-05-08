create_person = """
    create table if not exists Person (
        PersID integer primary key autoincrement,
        Nachname text,
        Vorname text,
        Strasse text,
        Plz text,
        Ort text
    )
    """

create_gebaeude = """
    create table if not exists Gebaeude (
        GebID integer primary key autoincrement,
        Bezeichnung text,
        Strasse text,
        Plz text,
        Ort text
    )
    """

create_merkmal = """
    create table if not exists Merkmal (
        MerkID integer primary key autoincrement,
        Merkmal text
    )
    """


create_raum = """
    create table if not exists Raum (
        RaumID integer primary key autoincrement,
        Typ text,
        GebID integer references Gebaeude(GebID) on delete cascade,
        MerkID integer references Merkmal(MerkID) on delete cascade
    )
    """

create_zugang = """
    create table if not exists Zugang (
        RaumID integer references Raum(RaumID) on delete cascade,
        PersID integer references Person(PersID) on delete cascade,
        ZeitVon text,
        ZeitBis text
    )
    """

fill_person_by_parameter = "insert into Person values (?,?,?,?,?,?)"
fill_zugang_by_parameter = "insert into Zugang values (?,?,?,?)"
fill_raum_by_parameter = "insert into Raum values (?,?,?,?)"
fill_gebaeude_by_parameter = "insert into Gebaeude values (?,?,?,?,?)"
fill_merkmal_by_parameter = "insert into Merkmal values (?,?)"

show_personen = "select * from Person"
show_zugang = "select * from Zugang"
show_raum = "select * from Raum"
show_gebaeude = "select * from Gebaeude"
show_merkmal = "select * from Merkmal"

enable_foreign_keys = "PRAGMA foreign_keys = TRUE;"
