# Question 1
first.matrix <- matrix(c(7,2,9,4,12,13), nrow = 2, ncol = 3)
first.matrix
second.matrix <- matrix(c(1,2,3,7,8,9,12,13,14,19,20,21), nrow = 3, ncol = 4)
second.matrix
result.matrix <- first.matrix%*%second.matrix
result.matrix

# Question 2

# Get amazon data
# getwd()
file <- read.csv('midterm_amz_data.csv')

#dim(file)
names(file)
# Check and clean the data

file$Order.Date <- as.POSIXlt(file$Order.Date)  
#file$Item.Total<-gsub("$","",as.character(file$Item.Total))
#file$Item.Subtotal<-gsub("$","",as.character(file$Item.Subtotal))

#file

print(paste('Max Price: ', max(file$Item.Total)))
print(paste('Min Price: ', min(file$Item.Total)))
print(paste('Median Price: ', median(file$Item.Total)))
print(paste('Mean Price: ', mean(file$Item.Total)))

month.df <- data.frame(
    month = c()
    )
months <- c('January', 'February', 'March', 'April', 'May', 'June',
           'July', 'August', 'September', 'October', 'November', 'December')
'
  for (i in months) {
    date <- 1
    for (x in file$Order.Date) {
      if (x == date) {
        month.df <- rbind(month.df, c(months[i]))
      }
      print(x)
      date <- date + 1
    }
    }
'

labels <- file$Category[c(0:length(file$Category))]
colors <- c('red', 'blue', 'yellow', 'green', 'white', 'light blue', 
            'black', 'pink', 'light green', 'orange', 'dark green')

pie(file$Item.Total, label = labels, main = 'Purchases by Category', col = colors)

"
labels <- months
colors <- c('red', 'blue', 'yellow', 'green', 'white', 'light blue', 
            'black', 'pink', 'light green', 'orange', 'dark green')

pie(file$Release.Date, label = labels, main = 'Purchases by Month', col = colors)
"

nums <- file$Item.Total[c(0:length(file$Item.Total))]
names <- file$Order.Date

barplot(nums, names.arg = names, density = 20)





