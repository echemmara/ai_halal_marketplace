# Evaluate model on validation data
validation_loss, validation_accuracy = model.evaluate(validation_generator)
print(f'Validation Loss: {validation_loss}, Validation Accuracy: {validation_accuracy}')
