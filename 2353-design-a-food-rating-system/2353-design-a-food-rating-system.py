class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodHash = defaultdict(list)
        self.rateHash = defaultdict(int)
        self.cuisHash = defaultdict(list)
        
        for food, cuis, rate in zip(foods, cuisines, ratings):
            
            self.foodHash[food].append(cuis)
            self.rateHash[food] = -rate
            heappush(self.cuisHash[cuis], (-rate, food))
        
    def changeRating(self, food: str, newRating: int) -> None:
        self.rateHash[food] = -newRating
        for cuis in self.foodHash[food]:
            heappush(self.cuisHash[cuis], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:

        while self.rateHash[self.cuisHash[cuisine][0][1]] != self.cuisHash[cuisine][0][0]:
            heappop(self.cuisHash[cuisine])
        
        return self.cuisHash[cuisine][0][1] if self.cuisHash[cuisine][0] else ""


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)