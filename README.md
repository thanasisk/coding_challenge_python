
Basket:
timestamp: Long
items: List[Item] (may contain duplicates)

    Item:
name: String
gtin: Int
price: Int

Promotion:
name: String
    discountPercent: Int (0-100)
gtins: Set[Int] (no duplicates)

    Redemption:
item: Item
    promotion: Promotion
saved: Int (item price * discountPercent/100)

    Given the model described above, implement a function "redeem" which processes a client's shopping basket, applying promotions to appropriate items, so that the total discount (sum of "saved" amounts) is maximal. The result of the function should be a list of Redemptions.

    function redeem(basket: Basket, promotions: List[Promotion]) : List[Redemption]

                                                                   Details:
                                                                   * a promotion is applicable only to items with the gtins it contains
                                                                   * a single promotion can be applied to one item only
                                                                   * one item can be redeemed with a single promotion only
                                                                   * multiple promotions may have non-disjoint sets of gtins, i.e. there may be different promotions applicable to the same item
                                                                   * the input list of promotions might contain duplicates - they can be applied independently to (same or different) applicable items.


                                                                   Example input (the format below is not precise, it’s just a concept example):

                                                                       Basket {
timestamp: 1004230459,
               items: [
                   item {
name: "toothpaste"
          gtin: 1001
          price: 120
                   },
               item {
name: "bread"
          gtin: 1002
          price: 100
               },
               item {
name: "bread"
          gtin: 1002
          price: 100
               },
               item {
name: "chicken nuggets"
          gtin: 1003
          price: 450
               }
           ]
                                                                       }

Promotions:
[
    promotion {
name: "Promo 1"
          discountPercent: 20
          gtins: [1001, 1002]
    },
    promotion {
name: "Promo 1"
          discountPercent: 20
          gtins: [1001, 1002]
    }
]

Example output:

Redemptions:
[
    redemption {
        item {
name: "toothpaste"
          gtin: 1001
          price: 120
        },
        promotion {
name: "Promo 1"
          discountPercent: 20
          gtins: [1001, 1002]
        },
saved: 24
    },
    redemption {
        item {
name: "bread"
          gtin: 1002
          price: 100
        },
        promotion {
name: "Promo 1"
          discountPercent: 20
          gtins: [1001, 1002]
        }
saved: 20
    }
]


This output maximizes the saved amount.
Selecting "chicken nuggets" would yield higher savings, but there is no promotion with the appropriate gtin.
Selecting "bread" twice, although allowed, would lead to lower total savings.
