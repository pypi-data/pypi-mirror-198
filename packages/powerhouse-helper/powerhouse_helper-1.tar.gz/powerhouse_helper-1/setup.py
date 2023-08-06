from setuptools import setup, find_namespace_packages

setup(name='powerhouse_helper',
      version='1',
      description='This is your console assistant by Python Powerhouse',
      author='Python Powerhouse',
      license='MIT',
      url = 'https://github.com/NovykovDaniil/python-core-project',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      packages=find_namespace_packages(),
      data_files=[('powerhouse_helper\\AddressBook\\address_saves', ['powerhouse_helper\\AddressBook\\address_saves\\address_book_auto_save.bin', 'powerhouse_helper\\AddressBook\\address_saves\\address_book.log']),
                  ('powerhouse_helper\\NoteBook\\note_saves', ['powerhouse_helper\\NoteBook\\note_saves\\note_book_auto_save.bin', 'powerhouse_helper\\NoteBook\\note_saves\\note_book.log']),
                  ('powerhouse_helper\\GameGooseKiller\\font', ['powerhouse_helper\\GameGooseKiller\\font\\UA Propisi.ttf']),
                  ('powerhouse_helper\\GameGooseKiller\\image', ['powerhouse_helper\\GameGooseKiller\\image\\background.png', 'powerhouse_helper\\GameGooseKiller\\image\\bonus.png', 'powerhouse_helper\\GameGooseKiller\\image\\boom.png', 'powerhouse_helper\\GameGooseKiller\\image\\enemy.png', 'powerhouse_helper\\GameGooseKiller\\image\\Farm-Goose.ico', 'powerhouse_helper\\GameGooseKiller\\image\\gameover.png']),
                  ('powerhouse_helper\\GameGooseKiller\\image\\background', ['powerhouse_helper\\GameGooseKiller\\image\\background\\1-1.png', 'powerhouse_helper\\GameGooseKiller\\image\\background\\1-2.png', 'powerhouse_helper\\GameGooseKiller\\image\\background\\1-3.png']),
                  ('powerhouse_helper\\GameGooseKiller\\image\Goose', ['powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-1.png', 'powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-2.png', 'powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-3.png', 'powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-4.png', 'powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-5.png'])],
      include_package_data=True,
      include_dirs = True,
      entry_points={'console_scripts': [
          'powerhouse-helper=powerhouse_helper.main:run']}
      )