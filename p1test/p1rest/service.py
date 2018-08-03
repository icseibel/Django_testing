from p1.models import Medicine, MedicineSchedule

def getScheduleByMedicine(medicine_id):
    """ get Medicine Schedules base on filters """
    medicine = Medicine.objects.get(pk=medicine_id)
    return MedicineSchedule.objects.filter(medicine=medicine)
