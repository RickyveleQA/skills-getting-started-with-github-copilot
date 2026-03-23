def test_signoff_successful(client, reset_activities):
    """Test successful unregister from activity"""
    # Arrange
    email = "michael@mergington.edu"  # Already in Chess Club
    activity = "Chess Club"
    
    # Act
    response = client.delete(
        f"/activities/{activity}/signoff",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert "Unregistered" in response.json()["message"]


def test_signoff_not_registered(client):
    """Test signoff for non-registered student"""
    # Arrange
    email = "nonexistent@mergington.edu"
    activity = "Chess Club"
    
    # Act
    response = client.delete(
        f"/activities/{activity}/signoff",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"].lower()


def test_signoff_activity_not_found(client):
    """Test signoff from non-existent activity"""
    # Arrange
    email = "test@mergington.edu"
    invalid_activity = "InvalidClub"
    
    # Act
    response = client.delete(
        f"/activities/{invalid_activity}/signoff",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
