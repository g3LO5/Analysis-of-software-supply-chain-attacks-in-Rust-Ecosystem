// Copyright (c) Microsoft Corporation. Licensed under the MIT License.

namespace Microsoft.CST.OpenSource.Model.Enums;

/// <summary>
/// Enum for information about when a package no longer exists on a package manager.
/// </summary>
public enum PackageRemovalReason
{
    /// <summary>
    /// When the package was unpublished from the repository/registry by someone.
    /// </summary>
    PackageUnpublished,

    /// <summary>
    /// When the package/version was removed from the repository/registry by the package manager's administrators.
    /// </summary>
    RemovedByRepository,
}