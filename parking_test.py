import pytest
import parking
class Test:

    @pytest.fixture
    def dict_te(self):
        p=parking.Parking()
        return p


    def test_park1(self,dict_te):
        carno="MH12ER2323"
        dict_te.park(carno)
        assert dict_te.lot[1]=="MH12ER2323"
        assert dict_te.lot[2]=="free"

    def test_park2(self,dict_te):
        carno = "98oi98oi9"
        dict_te.park(carno)
        assert dict_te.lot[1] == "free"

    def test_park3(self):
        carno0 = "MH12RT2323"
        carno1 = ""
        carno2 = "mh12RT2460"
        carno3 = "wewewewewe"
        carno4 = "3434343434"
        assert len(carno0) == 10
        assert len(carno1) != 10
        assert len(carno2) == 10
        assert len(carno3) == 10
        assert len(carno4) == 10








