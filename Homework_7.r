# Question 1

# A

df <- data.frame(
  id = 1:5,
  name = c('Peter', 'Amy', 'Ryan', 'Gary', 'Michelle'),
  salary = c(623.30, 515.20, 611.00, 729.00, 843.25)
)
df

# B
df1 <- data.frame( 
    department = c('Operations', 'Finance', 'Marketing', 'Security', 'Management')
    )
df2 <- cbind(df, df1)
df2

# C

df3 <- c(df$salary[c(1,4,5)], df$name[c(1,4,5)])
df3

# D
nums <- df$salary[c(1,4,5)]
names <- df$name[c(1,4,5)]

barplot(nums, names.arg = names, density = 15)

# E
dfpie <- c(max(df$salary), min(df$salary), median(df$salary))

labels <- c('Highest', 'Lowest', 'Median')
colors <- c('red', 'blue', 'yellow')

pie(dfpie, label = labels, main = "Pie Chart", col = colors)
legend("bottomright", labels, fill = colors)


# Question 2
library(TurtleGraphics)

turtle_init(width = 200, height = 200, mode = 'clip')
turtle_hide()

draw.rectangle <- function(length,height,color) {
    turtle_col(color)
    turtle_do({
    for (i in range(2)){
        turtle_forward(length)
        turtle_right(90)
        turtle_forward(height)
        turtle_right(90)
    }
    })
    }
        
draw.star <- function(size,color) {
    turtle_forward(0.5*size)
    turtle_right(162)
    turtle_col(color)
    turtle_do({
    for (i in range(10)){
        turtle_forward(size)
        turtle_right(144)
        turtle_left(162)
        turtle_backward(0.5*size)
    }
    })
    }

draw.rectangle(50, 100, 'red')
draw.star(25, 'red')
