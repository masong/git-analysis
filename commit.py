import common
from parent_relationship import parent_relationship_table
from patch import Patch

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref, relation

class Commit(common.Base):
  __tablename__ = 'commits'

  id = Column(Integer, primary_key=True)
  message = Column(String)
  time = Column(Integer)
  hash = Column(String, index=True, unique=True)
  patch_id = Column(Integer, ForeignKey('patches.id'))
  patch = relationship('Patch', backref='commit')
  committer_email = Column(String, ForeignKey('authors.email'))
  author_email = Column(String, ForeignKey('authors.email'))
  parents = relation('Commit', secondary=parent_relationship_table,
      primaryjoin=parent_relationship_table.c.child_hash==hash,
      secondaryjoin=parent_relationship_table.c.parent_hash==hash,
      backref='children')

  def __init__(self, message, time, hash, diff, committer_email, author_email):
    self.message = message
    self.time = time
    self.hash = hash
    self.patch = Patch(diff)
    self.committer_email = committer_email
    self.author_email = author_email

  def __repr__(self):
    return '<Commit(%s, %s, %s, %s)>' % (self.message, self.time, self.committer_email, self.author_email)
