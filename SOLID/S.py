"""
S - Single Responsibility Principle
Also known as Separation of Concerns Principle.

S in SOLID stands for Single Responsibility Principle.
This principle states that a class should have only one responsibility, 
only one reason to change. This means that a class should have only one job.
"""

from pathlib import Path


class JournalA:
	"""
	Here the JournalA class does not break the Single Responsibility Principle.
	Because it only has one job, which is to keep journal entries in memory.
	"""
	def __init__(self):
		self.entries = []
		self.count = 0
	
	def __str__(self):
		return "\n".join(self.entries)

	def add_entry(self, text: str):
		self.count += 1
		self.entries.append(f"{self.count}: {text}")

	def remove_entry(self, pos: int):
		try:
			del self.entries[pos]
		except IndexError:
			pass
	

"""
An example of god object, this is an anti pattern .
A god object is an object that does everything.
God object, bad!!!
"""
class JournalB:
	"""
	Here the JournalB class breaks the Single Responsibility Principle.
	Because it has more than one jobs to do:
		1. Keep journal entries in memory.
		2. Load journal entries from disk/url.
		3. Persist journal entries to disk.
	
	So, the problem will arise when we will have multiple classes and we 
	do the same operations like loading, saving, etc. Then we will have to
	write the same methods in all classes like load(), save(), etc. This is not
	so bad until we have to change the way we load or save the data. Then we will
	have to change the methods in all classes. We might forget to change it everywhere. 
	This is tedious and error prone. This is not good.
	"""
	def __init__(self):
		self.entries = []
		self.count = 0
	
	def __str__(self):
		return "\n".join(self.entries)

	def add_entry(self, text: str):
		self.count += 1
		self.entries.append(f"{self.count}: {text}")

	def remove_entry(self, pos: int):
		try:
			del self.entries[pos]
		except IndexError:
			pass
	
	def load(self, filepath: Path):
		pass

	def save(self, filepath: Path):
		pass

	def load_from_url(self, url: str):
		pass


class FilePersistenceManager:
	"""
	Here the FilePersistenceManager class does not break the Single Responsibility Principle.
	Because it only one job to persist the journals.

	Well technically it has two jobs:
		1. Save the journal to file.
		2. Load the journal from file.
	
	But it is okay to have two jobs in this case. Because both of the jobs are related to
	persisting the journal in file.

	To make it more maintainable when the project grows. And to follow the Single Responsibility 
	Principle more strictly, this could further be broken down into two classes to do the two jobs:
		1. Save the journal to file.
		2. Load the journal from file.
	"""
	@staticmethod
	def save_to_file(journal: JournalA, filepath: Path):
		with open(filepath, "w") as f:
			f.write(str(journal))

	@staticmethod
	def load_from_file(filepath: Path) -> JournalA:
		journal = JournalA()
		with open(filepath) as f:
			for line in f.readlines():
				journal.add_entry(line.strip())
		return journal
		