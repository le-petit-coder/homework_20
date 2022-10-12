from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_d):
        try:
            ent = Genre(**genre_d)
            self.session.add(ent)
            self.session.commit()
            return ent
        except Exception as es:
            self.session.rollbakc()
            return False

    def delete(self, rid):
        try:
            genre = self.get_one(rid)
            self.session.delete(genre)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

    def update(self, genre_d):
        try:
            genre = self.get_one(genre_d.get("id"))
            genre.name = genre_d.get("name")

            self.session.add(genre)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
