class DuplicateFilter:


    def clean(self, rectangles):

        result = []


        for r in rectangles:

            duplicate = False


            for old in result:

                if (
                    abs(r.x-old.x)<5
                    and
                    abs(r.y-old.y)<5
                    and
                    abs(r.width-old.width)<10
                    and
                    abs(r.height-old.height)<10
                ):
                    duplicate=True
                    break


            if not duplicate:
                result.append(r)


        return result