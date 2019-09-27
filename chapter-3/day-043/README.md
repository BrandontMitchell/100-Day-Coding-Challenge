# Day 043 - Flexbox Froggy

The purpose of this day is to introduce one of the most useful libraries built into CSS. If you completed the previous day's challenge
then you have probably noticed that centering and moving elements around with CSS can be extremely tedious, and often requires a guess-and-check type of strategy.

![Image of CSS](https://github.com/BrandontMitchell/100-Days-CC/blob/master/images/css.gif)

**Flexbox** is a set of CSS properties useful for aligning block level content into various layouts. It can help manage how the elements should be sized relative to each other. Similarly to the `position` property, you have to think about your content in terms of the elements themselves, as well as the containers that they're in.

## Starter Code

For this week, there isn't any starter code; the challenge will be to complete the all the levels on [flexboxfroggy.com](flexboxfroggy.com). This interactive game is a fun and engaging resource for learning how to use flexbox. After reading through the
**Getting Started** section, you can navigate to the website and attempt the challenge. 
  
## Getting Started
  
When you set a parent to `display: flex;` all items inside of it become **flex-items**. From there, you now have access to all of the flexbox CSS properties to easily customize the layout of your content.

### Basic properties for the flex container

```
display: flex;
```
Makes an element a **flex-container** and all of the items inside of it **flex-items**.

```
justify-content: flex-end; (flex-start, space-around,...)
```
Indicates how to space the items inside of the container along the main axis (usually horizontally).

```
align-items: flex-end; (flex-start, center, baseline,...)
```
Indicates how to space the items inside the container along the cross-axis (usually vertically).

```
flex-direction: row; (column)
```
Indicates whether a container flows horizontally or vertically.

### Basic properties for the flex item

```
flex-basis: 20%; (3em, 50px,...)
```
Indicates the default size of a flex-item 

```
align-self: flex-end; (flex-start, center, stretch,...)
```
Indicates whether to place this specific flex-item along the cross-axis.


### Extra Information

It can be difficult to visualize what each of these properties actually do without seeing it in action. This [tutorial](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) goes into a deeper explanation of the flex properties, with great visual examples. It's a great thing to bookmark and reference in the future.
