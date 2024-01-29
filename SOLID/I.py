"""
I - Interface Segregation Principle

I in SOLID stands for Interface Segregation Principle. This principle states that
we should not force any client to implement an interface which is irrelevant to
them. Instead, we should break up the interfaces into smaller ones, so that the
clients can only implement the interface that are relevant to them.
"""

from abc import ABC, abstractmethod


"""
Here we have a Machine class, which has three methods: print, fax, and scan. Now, if we
want to implement a multifunction printer, then we can inherit from this Machine class
and implement all the methods. But if we want to implement an old-fashioned printer, then
we have to implement all the methods, even though we don't need them. This is a violation
of the Interface Segregation Principle.
"""
class Machine(ABC):
	@abstractmethod
	def print(self, document):
		pass

	@abstractmethod
	def fax(self, document):
		pass

	@abstractmethod
	def scan(self, document):
		pass


"""
Here we have a multifunction printer, which implements all the methods of the Machine
class. This is fine, because we need all the methods in this class.
"""
class MultiFunctionPrinter(Machine):
	def print(self, document):
		pass

	def fax(self, document):
		pass

	def scan(self, document):
		pass


"""
Here we have an old-fashioned printer, which implements only the print method of the
Machine class. This is fine, because we only need the print method in this class.
"""
class OldFashionedPrinter(Machine):
	def print(self, document):
		# ok - print stuff
		pass

	def fax(self, document):
		pass  # do-nothing

	def scan(self, document):
		"""Not supported!"""
		raise NotImplementedError('Printer cannot scan!')



"""
A better approach is to break up the Machine class into smaller interfaces, so that the
clients can implement only the interfaces that are relevant to them. 

Here we have a Printer interface, which has only the print method, we have a Scanner interface, 
which has only the scan method and we have a Fax interface, which has only the fax method. Now, 
if we want to implement a multifunction printer, then we can inherit from all the three interfaces 
and implement all the methods. But if we want to implement an old-fashioned printer, then we can 
inherit from only the Printer interface and implement only the print method. 

This is a better approach, because we are not forcing the clients to implement 
the methods that they don't need.
"""
class PrinterInterface(ABC):
	@abstractmethod
	def print(self, document): pass
	
class ScannerInterface(ABC):
	@abstractmethod
	def scan(self, document): pass

class FaxInterface(ABC):
	@abstractmethod
	def fax(self, document): pass


# Not forced to implement methods that are not needed
class OldPrinter(PrinterInterface):
	def print(self, document):
		print(document)

# Forced to implement methods that are asked for by the interface inheritance
class ModernPrinter(PrinterInterface, ScannerInterface, FaxInterface):
	def print(self, document):
		print(document)

	def scan(self, document):
		print(document)

	def fax(self, document):
		print(document)
