# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sqla_fancy_core']

package_data = \
{'': ['*']}

install_requires = \
['sqlalchemy']

setup_kwargs = {
    'name': 'sqla-fancy-core',
    'version': '0.2.0',
    'description': 'SQLAlchemy core, but fancier',
    'long_description': '# sqla-fancy-core\n\nSQLAlchemy core, but fancier.\n\n```python\nimport sqlalchemy as sa\n\nfrom sqla_fancy_core import TableFactory\n\nmetadata = sa.MetaData()\ntf = TableFactory()\n\n# Define a table\nclass Author:\n\n    id = tf.auto_id()\n    name = tf.string("name")\n    created_at = tf.created_at()\n    updated_at = tf.updated_at()\n\n    Table = tf("author", metadata)\n\n# Define a table\nclass Book:\n\n    id = tf.auto_id()\n    title = tf.string("title")\n    author_id = tf.foreign_key("author_id", Author.id)\n    created_at = tf.created_at()\n    updated_at = tf.updated_at()\n\n    Table = tf("book", metadata)\n\n# Create the tables\nengine = sa.create_engine("sqlite:///:memory:")\nmetadata.create_all(engine)\n\nwith engine.connect() as conn:\n    # Insert author\n    qry = (\n        sa.insert(Author.Table)\n        .values({Author.name: "John Doe"})\n        .returning(Author.id)\n    )\n    author = next(conn.execute(qry))\n    (author_id,) = author\n    assert author_id == 1\n\n    # Insert book\n    qry = (\n        sa.insert(Book.Table)\n        .values({Book.title: "My Book", Book.author_id: author_id})\n        .returning(Book.id)\n    )\n    book = next(conn.execute(qry))\n    (book_id,) = book\n    assert book_id == 1\n\n    # Query the data\n    qry = sa.select(Author.name, Book.title).join(\n        Book.Table,\n        Book.author_id == Author.id,\n    )\n    result = conn.execute(qry).fetchall()\n    assert result == [("John Doe", "My Book")], result\n```\n',
    'author': 'Arijit Basu',
    'author_email': 'sayanarijit@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
