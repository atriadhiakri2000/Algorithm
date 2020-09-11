def addPolynomial(p1, p2):
    prev=None
    if(p1.power<p2.power):
        return addPolynomial(p2, p1)
    while(p1 is not None and p1.power>p2.power):
        p1=p1.next
    while(p1 is not None and p2 is not None):
        p1.coef=p1.coef+p2.coef
        prev=p1
        p1=p1.next
        p2=p2.next
    if poly2 is not None:
        prev.next = poly2
    head=p1
    ans_list = []
    while(head is not None):
        term = ""
        term += str(head.coef)
        if head.power != 0:
            term += "x^"
            term +=  str(head.power)
        ans_list.append(term)
        head = head.next
    ans = " + ".join(ans_list)
    print(ans)
