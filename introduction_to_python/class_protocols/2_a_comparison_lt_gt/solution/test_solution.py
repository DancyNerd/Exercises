def test_solution():
    from solution import Vector3D

    vec1 = Vector3D(1, 5, 3)
    vec2 = Vector3D(4, 4, 1)
    vec3 = Vector3D(1, 5, 2)

    assert not (vec1 < vec2)
    assert not (vec1 < vec3)
    assert vec3 < vec1
    assert vec2 < vec1

    assert not (vec2 > vec1)
    assert not (vec3 > vec1)
    assert vec1 > vec3
    assert vec1 > vec2
