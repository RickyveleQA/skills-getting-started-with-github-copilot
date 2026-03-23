def test_get_activities(client):
    """Test retrieving all activities"""
    # Arrange - nothing needed, activities are pre-populated
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "Programming Class" in data


def test_get_activities_has_required_fields(client):
    """Test that activities have required fields"""
    # Arrange
    required_fields = ["description", "schedule", "max_participants", "participants"]
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    for activity_name, activity in data.items():
        for field in required_fields:
            assert field in activity, f"Missing field '{field}' in {activity_name}"
