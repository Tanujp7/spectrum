from items.models import UserProfile, PersonalDetails
from recommenders.models import KeyToUserLink, UserToUserLink

class UserSimilarity:

    def __init__(self, user1=None, user2=None):
        self.u1 = user1
        self.u2 = user2
        self.up1 = PersonalDetails.objects.get(user=self.u1)
        self.up2 = PersonalDetails.objects.get(user=self.u2)

    def calculate(self):
        def nearly_equal(a,b,sig_fig=1):
            return ( a==b or
                     int(a*10**sig_fig) == int(b*10**sig_fig)
                   )

        def floaty(a,b,m=10):
            return (float(a)-float(b))/m

        marital_score = 1.0 if self.up1.marital_status == self.up2.marital_status else 0.0

        kids_score = 1.0 if self.up1.no_of_kids == self.up2.no_of_kids else 0.0
        if nearly_equal(self.up1.no_of_kids, self.up2.no_of_kids):
            kids_score += floaty(self.up1.no_of_kids, self.up2.no_of_kids, 10)
        kids_score /= 2

        score = ((marital_score + kids_score)/2)
        if score > 1:
            score = 1.0
        else if score < 0:
            score = 0.0

        return score

    def _get(self, weight=None):
        UserToUserLink.objects.create(item1=self.u1, item2=self.u2, raw_weight=weight, calculated_weight=weight, origin='User Similarity')

    def analyse(self):
        score = self.calculate()
        if score >= 0.5:
            self._get(weight=score)


def migrate_u2u():
    users = UserProfile.objects.all()

    for i in users:
        for j in users:
            if i.user != j.user:
                if not i.stop_usersim:
                    print('Initiating User Similarity.. for ' + str(i) + ' and ' + str(j))
                    u = UserSimilarity(user1=i,user2=j)
                    u.analyse()
        i.stop_usersim = True
        i.save()
