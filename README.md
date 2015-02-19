# descriptor-blog-demo
Python code accompanying a [blog post on descriptors](http://www.geekofalltrades.info/post/111422988392/python-the-deceptive-descriptor).

I create a chess piece that stores its rank and file position on the board.
I then modify that chess piece so that it stores rank and file in properties
that are capable of validating the values assigned to them, assuring that they
correspond to actual spaces on the chessboard.
I expand the chess game to four dimensions (because I'm a masochist), and
show how we can replace the increasingly-redundant property code with
instances of a single descriptor.
