# django-translation-model

## Django i18n support
I have created a `book name` translation model according the requirement I have added a json field in the model called `book_name` and update the field in django admin from one json field into multiple character field also I have added py test cases for that.

### How to run the project
1. clone the project
2. Change your current directory <br>
```cd book_shop```
3. Create a .env file from the .env.example file <br>
``cp .env.example .env``
4. Run build and do the setup <br>
```make build```
5. Run your server <br>
```make runserver```
6. Open a new terminal Create the database <br>
```make init-db```
7. Migrate django models in your database <br>
```make migrate```
8. Stop your old container and again run your server <br>
```make runserver```
9. To create the superuser or admin
```make superuser```

## Trees (optional)
### How would you implement such a data model in any RDBMS? Please provide your thoughts or even add a simple code snippet (Django-based would be great)
To implement hierarchical data in a database MPTT(Modified Preorder Tree Traversal) is good way. which provide us very efficient way to make retrieval operations.
	it has some feature which make it more efficient like 
1. The tree structure is automatically updated when you create or delete model instances, or change an instance’s parent.
2. Each level of the tree is automatically sorted by a field (or fields) of your choice.
	Model Representation:-

		from mptt.models import MPTTModel, TreeForeignKey

		class Alphabet(MPTTModel):
		    name = models.CharField(max_length=25, unique=True)
		    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

		    class MPTTMeta:
			level_attr = 'mptt_level'
			order_insertion_by=['name']


		Here,
		level_attr indicates root nodes would have a level of 0 and their immediate children would have have a level of 1(Defaults to 'level').
		
		order_insertion_by tell A list of field names which should define ordering when new tree nodes are being inserted or existing nodes are being reparented, with the most significant 				ordering field name first. Defaults to []

### What are possible approaches and pros/cons?
First approache may be to go with django models's ForeignKey where manually set child_node with ForeignKey and update this node with it's respected events.
#### Some advantages(pros) 
1. simple code snippet
#### Disadvantages(cons) 
1. hard to understand flow
2. hard to traverse node
3. tuff to manage node wile insert or delete node from middle.
4. hard queryset to get node info.
	
	
### How would you count number of descendants (e.g., for A count B + D + E) of any node on the first level?
	Genre.get_descendant_count(c)

### How does D node relate to A node?
	D.is_descendant_of(A)