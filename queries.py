create_person = """
    create table if not exists Person (
        PersID TEXT,
        Nachname text,
        Vorname text,
        Strasse text,
        Plz text,
        Ort text
    )
    """

create_zugang = """
    create table if not exists Zugang (
        RaumID text,
        PersID text,
        ZeitVon text,
        ZeitBis text
    )
    """

create_raum = """
    create table if not exists Raum (
        RaumID text,
        Typ text,
        GebID text,
        MerkID text
    )
    """

create_gebaeude = """
    create table if not exists Gebaeude (
        GebID text,
        Bezeichnung text,
        Strasse text,
        Plz text,
        Ort text
    )
    """

create_merkmal = """
    create table if not exists Merkmal (
        MerkID text,
        Merkmal text
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
