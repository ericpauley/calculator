## PYTHON GRAPHING CALCULATOR ##

### CONTENTS ###
1. Installing Program
2. Basic Input
3. Functions
3. A Physics Example

### 1. Installing Program ###
The program is distributed as an executable (.exe) file. No additional installation is required. Just double click on the file to run.

###2. Basic Input ###
The calculator screen contains a text box on the bottom with lists of previous inputs and outputs on the top. To compute something in the calculator simply enter the expression in the bottom bar and press `ENTER`.

The Calculator accepts basic mathematical notation. For example, try entering `1+1` into the bar and pressing `ENTER`. The input will show on the screen as well as the result, `2`.

#### Variables ####
The calculator also accepts the use of variables. You may enter symbolic expressions into the bar to evaluate them. For example, entering the expression `(2x-3)/5` into the bar will cause the expression to be distributed and evaluated to `2*x/5 - 3/5`. In this way math may be done with one or more symbols.

#### Answer Variable ####
The `ans` variable will always hold the result of the latest calculation. This is useful for performing multiple dependent calculations in succession.

#### Units ####
The calculator has the ability to do math with metric and English units. For example try entering `5kg*3m/s^2`, representing the force needed to accelerate an object of mass `5kg` at `3m/s^s`. The calculator should return the result `15kg*m/s**2`. Should a unit interfere with some other quantity, all units can be accessed by prefixing their name with `u`. (For example, `u.kg*u.m/u.s^2`)

#### Assignment of variables ####
While the calculator does symbolic math by default, variables may be assigned values at any point, using the equals sign (`=`). For example, running the command `a = 2` will set `a` to `2` so that running the command `5a` after it will return 10. In this way values may be stored and reused in later operations, supplementing the `ans` variable.

#### A Note on symbols ####
Because the calculator is a simplified Python prompt, there are a few differences between its math notation and standard notation. Whereas a carrot (`^`) is normally used to denote powers in math, the calculator will represent powers as two asterisks (`**`). Inputs containing a carrot will still be parsed correctly.

The calculator also uses a different notation for equality, two equals signs (`==`). For purposes of testing if two things are equal these two signs are used, but to assign a value to a variable just one equals sign (`=`) is used.

### 3. Functions ###
One of the most powerful features of this calculator is its ability to hook into various functions in order to provide further functionality. Below a small subset of those functions are detailed. For more information visit the SymPy docs at http://docs.sympy.org/latest/index.html.

Functions are run by typing their name, followed by parentheses with the arguments to that function enclosed. For example, `solve(3x-1==0)` will run the `solve` function with the equation `3x-1==0`.

#### solve ####
This calculator has the ability to take symbolic equations and find the resulting values which make that equation true. For example, try running `solve(3x-3==0)`. This will return `[1]`, the list of the solutions to the equation. In this case there is only one solution but for more complicated equations the calculator can find any number of equations for any number of variables.

The calculator can also solve multiple equations for multiple variables. For example, try running `solve([3x-4==y, 2x+3==y],[x,y])`. This will solve the two equations entered for both `x` and `y`. The result, `{x: 7, y: 17}` shows that `x==7` and `y==17`. In this way complex equation systems may be solved quickly and easily.

#### diff ####
The calculator has the ability to take the derivative of equations multiple times and with respect to any variable. This is a very powerful tool in calculus and only the most expensive graphing calculators on the market have the ability to do it. To try it out, try entering `diff(3x^2-2x+1)`. It should equal `6*x - 2`, the derivative of the original function with respect to x.

The calculator will try to figure out what you want to take the derivative with respect to, but in case you want to take more complex derivatives you may enter the variables to differentiate with respect to as more arguments. `diff(3x^2*y+6y^2*x, y, x)` will find the differential with respect to x and y symbolically. This is known as the gradient in mathematics and is usually very tedious to calculate. With the calculator is is now just one command.

#### integrate ####
Integration is one of the most powerful tools in all of mathematics, and the calculator has the ability to perform complex symbolic integrations on just about anything. Try running `integrate(16x^2+12x-16)`, which returns `16*x**3/3 + 6*x**2 - 16*x`. This method will work with very complex equations thanks to a state-of-the-art symbolic math library with the program utilizes. You may also integrate over multiple variables in the same way you would differentiate over multiple variables.

### A Physics Example ###
Assume an object is thrown upwards at `15m/s`. How long will it take for the object to fall?

This problem is trivial to solve with the calculator:

1. Set `a` to the acceleration of gravity: `a = -9.8m/s^2`
2. Integrate `a` with respect to `t` and add initial velocity: `v = integrate(a, t) + 15m/s`
3. Integrate velocity to find position: `y = integrate(v, t)`
4. Solve the final equation to get the time when `y == 0`: `solve(y == 0, t)`

This final equation returns `[0.0, 3.06122448979592*s]`. The first value is at the time the object is thrown and the final value is the amount of time it takes for the object to land.
