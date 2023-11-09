class BuildingError(Exception):
    def __str__(self):
        return f"Занадто мало матеріалів для того, щоб побудувати будинок"
def check_material(amoutn_of_material, limit_value):
    if amoutn_of_material > limit_value:
        return "матеріалів достатньо"
    else:
        raise BuildingError(amoutn_of_material)
matterial = 100
print(check_material(matterial, 300))