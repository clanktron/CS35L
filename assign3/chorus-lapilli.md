# Chorus Lapilli

To start Chorus Lapilli I simply copied the entire project of tictactoe.

>Make sure to delete the node_modules folder and run `npm install` to get all the dependencies for the application.

To test the source code for the app locally simply run `npm start` inside the main directory.

Alternatively, use the dockerfile provided to build and run an image locally.

```dockerfile
FROM node:lts-alpine

WORKDIR /app

COPY . .

CMD ["npm", "start"]
```

```sh
$ docker build -t choruslapilli .
$ docker run -p 3000:3000 choruslapilli
```

Interacting with the game is the same as the original tictactoe. Simply 
take turns taking your move and play until someone wins! The game will 
notify you of such
and prevent any "illegal" moves by default
Amending the tictactoe game with no previous react experience was rather challenging. It initially consisted of 
extensive trial and error but eventually proved to be a relatively minor feat. The key to such a deeper 
understanding of how state is handled in the react ecosystem. After this exercise it seems pertinent to keep 
state as close as possible to the root element of the project. This prevents unecessary *prop drilling and keeps 
a few central componets as the single "source of truth".

*prop drilling: passing data through nested child components 

Majority of the modifications to the program were solved by adding a new stateful object to the mix. I called
this object `origin` and it contained any information I needed concerning the state of the game. 

```javascript
    const [origin, setOrigin] = useState({
        selected: false,
        originSquare: null
    });
```

The rest of the implementation was handled with further logic in the `HandleClick()` function.
Checking for when a piece was selected by a valid player had to be done etc. The code for such can be seen below.
You'll notice the `console.logs` to be very prevalent. I used these in lieu of proper debugging as I do not have 
extensive experience with the browser debugger (I couldn't get it to recognize objects or variables?).
The general logic consists of checking if 6 pieces have been placed, and then transitioning to check that a user
has selected a valid origin and target square for their piece.

```javascript
    function handleClick(i) {
        if (calculateWinner(squares)) return;
        const nextSquares = squares.slice();
        if (currentMove <= 5) {
            if (squares[i]) return;
            if (xIsNext) {
                nextSquares[i] = 'X';
            } else {
                nextSquares[i] = 'O';
            }
            setxIsNext(!xIsNext);
        }
        else {
            if (origin.selected === true) {
                if (nextSquares[i] === null && isAdjacent(origin.originSquare,i)){
                    if (xIsNext && squares[4] === 'X' || !xIsNext && squares[4] === 'O'){
                        let targetSquare = nextSquares[i]
                        let oldOrigin = nextSquares[origin.originSquare]
                        nextSquares[i] = (xIsNext ? 'X' : 'O');
                        nextSquares[origin.originSquare] = null;
                        if (calculateWinner(nextSquares) || origin.originSquare === 4) {
                            console.log("Moved ", (xIsNext ? 'X' : 'O'), " to square ", i)
                            setxIsNext(!xIsNext);
                        }
                        else {
                            console.log("You must move the center piece or win");
                            nextSquares[i] = targetSquare;
                            nextSquares[origin.originSquare] = oldOrigin;
                        }
                        setOrigin({ ...origin, selected: false});
                    }
                    else {
                        nextSquares[i] = (xIsNext ? 'X' : 'O');
                        nextSquares[origin.originSquare] = null;
                        setOrigin({ ...origin, selected: false});
                        console.log("Moved ", (xIsNext ? 'X' : 'O'), " to square ", i)
                        setxIsNext(!xIsNext);
                    }
                }
                else {
                    console.log("invalid square")
                    setOrigin({ ...origin, selected: false});
                }
            }
            else if (origin.selected === false) {
                if (xIsNext && nextSquares[i] === 'X' || !xIsNext && nextSquares[i] === 'O') {
                    setOrigin({ ...origin, selected: true, originSquare: i});
                    console.log(origin.originSquare)
                    console.log("Selected square ", i, " containing ", (xIsNext ? 'X' : 'O'), " to move to adjacent square.")
                }
            }
        }
        onPlay(nextSquares);
    }


```
