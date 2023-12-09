



Day 18 - Advent of Code 2015



window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});


# [Advent of Code](/)

* [[About]](/2015/about)
* [[Events]](/2015/events)
* [[Shop]](https://teespring.com/stores/advent-of-code)
* [[Settings]](/2015/settings)
* [[Log Out]](/2015/auth/logout)
weiss-i-net 11\*#        Î»y.[2015](/2015)

* [[Calendar]](/2015)
* [[AoC++]](/2015/support)
* [[Sponsors]](/2015/sponsors)
* [[Leaderboard]](/2015/leaderboard)
* [[Stats]](/2015/stats)




## --- Day 18: Like a GIF For Your Yard ---

After the [million lights incident](6), the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.


Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to *animation*.


Start by setting your lights to the included initial configuration (your puzzle input). A `#` means "on", and a `.` means "off".


Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".


For example, in a simplified 6x6 grid, the light marked `A` has the neighbors numbered `1` through `8`, and the light marked `B`, which is on an edge, only has the neighbors marked `1` through `5`:



```
1B5...
234...
......
..123.
..8A4.
..765.

```

The state a light should have next is based on its current state (on or off) plus the *number of neighbors that are on*:


* A light which is *on* stays on when `2` or `3` neighbors are on, and turns off otherwise.
* A light which is *off* turns on if exactly `3` neighbors are on, and stays off otherwise.


All of the lights update simultaneously; they all consider the same current state before moving to the next.


Here's a few steps from an example configuration of another 6x6 grid:



```
Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......

```

After `4` steps, this example has four lights on.


In your grid of 100x100 lights, given your initial configuration, *how many lights are on after 100 steps*?



To begin, [get your puzzle input](18/input).


Answer:  


You can also [Shareon
 [Twitter](https://twitter.com/intent/tweet?text=%22Like+a+GIF+For+Your+Yard%22+%2D+Day+18+%2D+Advent+of+Code+2015&url=https%3A%2F%2Fadventofcode%2Ecom%2F2015%2Fday%2F18&related=ericwastl&hashtags=AdventOfCode)
[Mastodon](javascript:void(0);)] this puzzle.





(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



